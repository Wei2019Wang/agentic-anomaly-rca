
from tools.metrics import get_timeseries, get_top_movers



def test_get_timeseries_deterministic():
    series1 = get_timeseries("RPM")
    series2 = get_timeseries("RPM")

    assert series1 == series2
    assert len(series1["values"]) == 7
    assert series1["metric"] == "RPM"



def test_get_top_movers_deterministic():
    movers1 = get_top_movers("RPM")
    movers2 = get_top_movers("RPM")

    assert movers1 == movers2
    assert len(movers1) > 0
    assert movers1[0]["dimension"] in {"country", "device"}

