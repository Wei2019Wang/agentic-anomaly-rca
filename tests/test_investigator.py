from agents.investigator import Investigator, InvestigationState, ToolCall

def dummy_timeseries(metric: str):
    return [1, 1, 10, 1] 



def dummy_zscore(window: int, threshold: float):
    return [2]

def test_investigator_runs():
    tools = {
        "get_timeseries": dummy_timeseries,
        "rolling_zscore": dummy_zscore
    }
    
    investigator = Investigator(tools)
    state = InvestigationState()

    state = investigator.step(
        state,
        thought="load data",
        action=ToolCall(name="get_timeseries", args={"metric": "rpm"})
    )

    state = investigator.step(
        state,
        thought="detect anomalies",
        action=ToolCall(name="rolling_zscore", args={"window": 3, "threshold": 2.0})
    )

    state = investigator.step(
        state,
        thought="done",
        action=None
        )

    assert state.done is True
    assert state.tool_calls == 2
    assert len(state.observations) == 2