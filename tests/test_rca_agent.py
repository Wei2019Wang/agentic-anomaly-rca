from rca.rca_agent import RCAAgent


def test_rca_agnet_basic_output():
    agent = RCAAgent(
        available_dims = ["country", "device", "supply_source"]

    )

    alert_id = "ALERT_TEST"
    anomalies = [2, 7]

    report = agent.explain(alert_id, anomalies)

    assert report.alert_id == alert_id
    assert len(report.explanations) == len(anomalies)

    for exp, anomaly_id in zip(report.explanations, anomalies):
        assert exp.anomaly_id == anomaly_id
        assert len(exp.dimensions) == 2
        assert isinstance(exp.explanation, str)
        assert 0.0 <= exp.confidence <= 1.0
