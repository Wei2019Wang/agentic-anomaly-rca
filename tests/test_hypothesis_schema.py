from utils.schemas import Hypothesis

def test_hypothesis_schema_valid():
    h = Hypothesis(
        cause="Weather",
        prior=0.4,
        score=0.4,
        required_evidence=["metrics_slice", "weather_signal"],
    )

    assert h.cause == "Weather"
    assert h.prior == 0.4
    assert h.score == 0.4
