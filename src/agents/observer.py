# src/agents/observer.py

from utils.schemas import RCAState
from utils.logging import get_logger
from tools.metrics import get_timeseries, get_top_movers


logger = get_logger(__name__)


def observe_anomaly(state: RCAState) -> RCAState:
    """
    Observe anomaly using deterministic metric tools.
    """
    series = get_timeseries(metric="RPM", days=7, seed=42)
    movers = get_top_movers(seed=42)

    state.observations =(
        f"RPM last 7 days: {series}."
        f"Top movers: {movers}."
    )

    logger.info(f"Observed anomaly with tools: {state.anomaly}")

    return state
