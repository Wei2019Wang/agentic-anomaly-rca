from graphs.rca_graph import build_rca_graph
from utils.schemas import RCAState


def test_retry_happens_when_critic_requests():
    graph = build_rca_graph()

    state = RCAState(
        alert_id="ALERT_1",
        anomaly="RPM dropped",
        max_retries=2,
    )

    result = graph.invoke(state)

    assert result["retries"] > 0


def test_retry_stops_at_max():
    graph = build_rca_graph()

    state = RCAState(
        alert_id="ALERT_2",
        anomaly="RPM dropped",
        max_retries=1,
    )

    result = graph.invoke(state)

    assert result["retries"] == 1



def test_unknown_after_exhausted_retries():
    graph = build_rca_graph()

    state = RCAState(
        alert_id="ALERT_3",
        anomaly="RPM dropped",
        max_retries=1,
    )

    result = graph.invoke(state)

    assert result["confidence"] == 0.0
    assert "UNKNOWN" in result["report"]
