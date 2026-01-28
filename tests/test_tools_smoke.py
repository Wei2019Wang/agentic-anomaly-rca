
from tools.metrics import get_timeseries, get_top_movers


def test_get_timeseries_deterministic():
    series1 = get_timeseries("RPM", seed=42)
    series2 = get_timeseries("RPM", seed=42)
    assert series1 == series2
    assert len(series1) == 7


def test_get_top_movers_deterministic():
    movers1 = get_top_movers(seed=42)
    movers2 = get_top_movers(seed=42)
    assert movers1 == movers2
    assert "Finance" in movers1
