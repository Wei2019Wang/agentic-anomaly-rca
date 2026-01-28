# src/agents/observer.py

from utils.schemas import RCAState
from tools.metrics import get_metric_timeseries


def observe_anomaly(state: RCAState) -> RCAState:
    """
    Observe the anomaly and produce initial observations.
    """

    anomaly = state["anomaly"]

    # Fake observation logic for now
    series = get_metric_timeseries("RPM")
    state["observations"] = f"RPM last 7 days: {series}"

    return state
