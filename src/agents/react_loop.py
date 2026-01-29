# Later, the LLM replaces these hardcoded thoughts/actions.

from agents.investigator import Investigator, InvestigationState, ToolCall


def run_react_loop(investigator: Investigator):
    state = InvestigationState()

    # step 1
    state = investigator.step(
        state,
        thought="IN shold load the time series",
        action=ToolCall(
            name="get_tieseries",
            args={"metric": "rpm"}
        )
    )

    # step2 
    state = investigator.step(
        state,
        thought="Check for anomalies using rolling z-score",
        action=ToolCall(
            name="rolling_zscore",
            args={"window": 5, "threshold": 3.0}
        )
    )

    # final step (no action)
    state = investigator.step(
        state,
        thought="Detected anomalies explain the spike; inevstigation complete.",
        action=None
    )

    return state
    