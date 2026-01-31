# src/tools/metrics.py


def get_timeseries(metric: str, window: int = 7):
    """
    Mock time series data for a metric.
    """
    return {
        "metric": metric,
        "window_days": window,
        "values": [100, 98, 95, 90, 88, 85, 87],
    }


def get_top_movers(metric: str, top_k: int = 5):
    """
    Mock top movers for a metric.
    """
    return [
        {"dimension": "country", "value": "US", "delta_pct": -12.3},
        {"dimension": "device", "value": "mobile", "delta_pct": -8.1},
    ][:top_k]