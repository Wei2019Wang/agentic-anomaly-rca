from tools.synthetic_data import generate_series_with_anomalies
from tools.detectors import rolling_zscore, rolling_mad


def test_rolling_zscore_detects_anomalies():
    series = generate_series_with_anomalies(seed=42)

    anomalies = rolling_zscore(series)

    assert len(anomalies) > 0
    assert len(anomalies) <= 20


def test_rolling_mad_detects_anomalies():
    series = generate_series_with_anomalies(seed=42)

    anomalies = rolling_mad(series)

    assert len(anomalies) > 0
    assert len(anomalies) <= 30
