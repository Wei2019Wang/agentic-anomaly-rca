# src/main.py
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
)

from graphs.rca_graph import build_rca_graph
from utils.schemas import RCAState
from utils.logging import get_logger


# find . -name "__pycache__" -type d -exec rm -r {} +

def create_initial_state(alert_id: str, anomaly: str) -> RCAState:
    return RCAState(
        alert_id=alert_id,
        anomaly=anomaly,
        observations=None,
        hypotheses=None,
        evidence=None,
        confidence=None,
        retries=0,
    )


if __name__ == "__main__":
    graph = build_rca_graph()

    initial_state = create_initial_state(alert_id="MAIN_ALERT_1", anomaly="RPM dropped 6% WoW")

    final_state = graph.invoke(initial_state)

    print(final_state)
