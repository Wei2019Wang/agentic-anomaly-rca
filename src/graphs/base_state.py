"""
Base state definition for the agentic root-cause analysis graph.

This module exposes the RCAState schema for LangGraph.
State contains data only and no control logic.
"""

from utils.schemas import RCAState
from typing import List
from pydantic import BaseModel, Field
from rca.schemas import Hypothesis, ToolInvocation


class RCAState(BaseModel):
    alert_id: str
    anomalies: List[int]
    priors: dict[str, float] | None = None
    hypotheses: List[Hypothesis] | None = None
    plan: List[ToolInvocation] | None = None


__all__ = ["RCAState"]
