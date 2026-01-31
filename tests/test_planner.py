from rca.planner import build_evidence_plan
from rca.schemas import Hypothesis


def test_planner_respects_priority_and_budget():
    hypotheses = [
        Hypothesis(cause="Weather", prior=0.1, score=0.1, required_evidence=[]),
        Hypothesis(cause="InfraLatency", prior=0.6, score=0.6, required_evidence=[]),
        Hypothesis(cause="ExperimentChange", prior=0.3, score=0.3, required_evidence=[]),
    ]

    plan = build_evidence_plan(hypotheses)

    assert len(plan) == 3
    assert plan[0].tool_name == "system.get_latency"

def test_empty_hypotheses_returns_empty_plan():
    assert build_evidence_plan([]) == []