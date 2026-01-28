# src/main.py

from graphs.rca_graph import build_rca_graph
from utils.schemas import RCAState


def create_initial_state(anomaly: str) -> RCAState:
    return {
        "anomaly": anomaly,
        "observations": None,
        "hypotheses": None,
        "evidence": None,
        "confidence": None,
        "retries": 0,
    }


if __name__ == "__main__":
    graph = build_rca_graph()

    initial_state = create_initial_state("RPM dropped 6% WoW")

    final_state = graph.invoke(initial_state)
    print(">>> main.py started")

    print(final_state)
