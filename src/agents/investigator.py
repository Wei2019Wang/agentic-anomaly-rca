from typing import List, Dict, Any
from pydantic import BaseModel, ValidationError

MAX_TOOL_CALLS = 5

class ToolCall(BaseModel):
    name: str
    args: Dict[str, Any]


class InvestigationState(BaseModel):
    thoughts: List[str] = []
    observations: List[str] = []
    tool_calls: int = 0
    done: bool = False
    result: str | None = None


class Investigator:
    def __init__(self, tools: Dict[str, callable]):
        self.tools = tools

    def step(self, state: InvestigationState, thought: str, action: ToolCall | None):
        state.thoughts.append(thought)

        if action is None:
            state.done = True
            state.result = thought
            return state
        
        if state.tool_calls >= MAX_TOOL_CALLS:
            raise RuntimeError("Max tool calls reached.")

        if action.name not in self.tools:
            raise ValueError(f"Tool {action.name} not found.")

        # execute tool
        result = self.tools[action.name](**action.args)
        
        state.tool_calls += 1

        state.observations.append(str(result))
        
        return state