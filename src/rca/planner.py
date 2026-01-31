from typing import List
from rca.schemas import Hypothesis, ToolInvocation

MAX_TOOL_CALLS = 3

def build_evidence_plan(
    hypotheses: List[Hypothesis],
) -> List[ToolInvocation]:
    plan: List[ToolInvocation] = []

    for h in sorted(hypotheses, key=lambda x: x.score, reverse=True):
        if len(plan) >= MAX_TOOL_CALLS:
            break

        if h.cause == "Weather":
            plan.append(
                ToolInvocation(
                    tool_name="get_weather_data", 
                    args={"region": "US"}
                )
            )

        elif h.cause == "InfraLatency":
            plan.append(
                ToolInvocation(
                    tool_name="system.get_latency",
                    args={"service": "ads"}     
                )
            )
        
        elif h.cause == "ExperimentChange":
            plan.append(
                ToolInvocation(
                    tool_name="experiments.get_changes",
                    args={"window": "24h"}
                )
            )

        elif h.cause == "AdvertiserPullback":
            plan.append(
                ToolInvocation(
                    tool_name="advertisers.get_spend_changes",
                    args={"top_k": 10}
                )
            )

        elif h.cause == "DataPipelineIssue":
            plan.append(
                ToolInvocation(
                    tool_name="system.get_pipeline_status",
                    args={}
                )
            )

    return plan
