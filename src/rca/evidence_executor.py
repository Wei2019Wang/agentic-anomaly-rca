from typing import List
from utils.schemas import ToolInvocation, Evidence
from tools import weather, experiments, advertisers, system
from mcp_adapters.tools import MCP_TOOLS

TOOL_REGISTRY = {
    "weather.get_events": weather.get_events,
    "experiments.get_changes": experiments.get_changes,
    "advertisers.get_spend_changes": advertisers.get_spend_changes,
    "system.get_latency": system.get_latency,
    "system.get_pipeline_status": system.get_pipeline_status,
}


def execute_plan(plan: List[ToolInvocation]) -> List[Evidence]:
    evidence: List[Evidence] = []

    for invocation in plan:
        # Handle both ToolInvocation objects and dicts (from serialization or tests)
        if isinstance(invocation, dict):
            tool_name = invocation.get("tool_name") or invocation.get("tool")
            args = invocation.get("args", {})
        else:
            tool_name = invocation.tool_name
            args = invocation.args

        try:
            # 🔹 1. MCP path (preferred if available)
            if tool_name in MCP_TOOLS:
                output = MCP_TOOLS[tool_name].invoke(args)
                citation = "mcp"

            # 🔹 2. Native Python fallback
            else:
                fn = TOOL_REGISTRY[tool_name]
                output = fn(**args)
                citation = "native"

            evidence.append(
                Evidence(
                    source=tool_name,
                    output=output,
                    citation=citation,
                    success=True,
                )
            )

        except Exception as e:
            evidence.append(
                Evidence(
                    source=tool_name,
                    output=str(e),
                    citation="error",
                    success=False,
                    error=str(e),
                )
            )

    return  evidence

