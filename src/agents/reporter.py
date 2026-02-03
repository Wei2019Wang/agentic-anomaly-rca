# src/agents/reporter.py

from utils.schemas import RCAState

def generate_report(state: RCAState) -> dict:
    """
    Generate a simple textual report from observations.
    """

    report = (
        f"Anomaly detected: {state.anomaly}. "
        f"Observations: {state.observations}"
    )

    return {
        "report": report,
        "confidence": 0.6
    }

def generate_unknown_report(state: RCAState) -> dict:
    report = (
        f"Anomaly detected: {state.anomaly}. "
        "Root cause could not be determined with sufficient confidence "
        "after multiple attempts. Marked as UNKNOWN."
    )
    return {
        "report": report,
        "confidence": 0.0
    }
