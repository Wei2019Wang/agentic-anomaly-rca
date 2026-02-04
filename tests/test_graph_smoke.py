from graphs.rca_graph import build_rca_graph
from utils.schemas import RCAState

def test_detect_to_report_flow():
    graph = build_rca_graph()

    state = RCAState(alert_id="TEST_ALERT_1", anomaly="RPM dropped")

    result = graph.invoke(state)
    print(result)
    assert result["report"] is not None
    assert "RPM dropped" in result["report"]