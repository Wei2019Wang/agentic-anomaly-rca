# src/agents/reporter.py

from utils.schemas import RCAState

def generate_report(state: RCAState) -> RCAState:
    """
    Generate a simple textual report from observations.
    """

    state.report = (
        f"Anomaly detected: {state.anomaly}. "
        f"Observations: {state.observations}"
    )

    state.confidence = 0.6

    return state