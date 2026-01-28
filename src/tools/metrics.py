# src/tools/metrics.py

from typing import List


def get_metric_timeseries(metric: str, days: int = 7) -> List[float]:
    """
    Return fake metric values for the past N days.
    Deterministic stub for development.
    """
    return [100.0, 98.5, 97.2, 95.0, 94.3, 94.0, 93.8]
