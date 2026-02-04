# src/agents/reporter.py

from utils.schemas import RCAState

def generate_report(state: RCAState) -> dict:
    # If we failed after retries → UNKNOWN
    if not state.hypotheses or state.confidence is None:
        return generate_unknown_report(state)

    top = max(state.hypotheses, key=lambda h: h.score)

    evidence_sources = [
        e.source for e in (state.evidence or []) if e.success
    ]

    report = (
        f"Alert {state.alert_id}: {state.anomaly}\n"
        f"Most likely root cause: {top.cause}\n"
        f"Supporting evidence: {evidence_sources}"
    )

    return {
        "alert_id": state.alert_id,
        "report": report,
        "confidence": round(top.score, 2),
    }

def generate_unknown_report(state: RCAState) -> dict:
    report = (
        f"Alert {state.alert_id}: {state.anomaly}\n"
        "Root cause could not be determined with sufficient confidence "
        "after multiple attempts. Marked as UNKNOWN."
    )
    return {
        "alert_id": state.alert_id,
        "report": report,
        "confidence": 0.0,
    }
