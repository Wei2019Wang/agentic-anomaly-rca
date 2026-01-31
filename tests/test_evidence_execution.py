from rca.executor import execute_plan


def test_tool_failure_is_captured():
    plan = [
        {"tool": "metrics.get_timeseries", "args": {"metric": "RPM"}},
        {"tool": "nonexistent.tool", "args": {}},
    ]

    evidence = execute_plan(plan)

    assert len(evidence) == 2
    assert evidence[1].success is False
    assert evidence[1].error is not None