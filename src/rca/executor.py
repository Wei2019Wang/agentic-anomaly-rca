from typing import Dict, List
from rca.evidence import Evidence
from tools import metrics, experiments, advertisers, weather


TOOL_REGISTRY = {
    "metrics.get_timeseries": metrics.get_timeseries,
    "metrics.get_top_movers": metrics.get_top_movers,
    "experiments.get_changes": experiments.get_changes,
    "advertisers.get_spend_changes": advertisers.get_spend_changes,
    "weather.get_events": weather.get_events,
}


def execute_plan(plan: List[Dict]) -> List[Evidence]:
    evidence_items: List[Evidence] = []

    for step in plan:
        tool_name = step["tool"]
        args = step.get("args", {})

        try:
            tool_fn = TOOL_REGISTRY[tool_name]
            result = tool_fn(**args)

            evidence_items.append(
                Evidence(
                    source=tool_name,
                    output=result,
                    citation=f"Tool {tool_name} executed with args {args}",
                )
            )

        except Exception as e:
            evidence_items.append(
                Evidence(
                    source=tool_name,
                    output=None,
                    citation=f"Tool {tool_name} failed",
                    success=False,
                    error=str(e),
                )
            )

    return evidence_items
