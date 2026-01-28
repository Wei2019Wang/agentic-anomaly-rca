# src/tools/metrics.py

from typing import List, Dict
import random

def get_timeseries(metric: str, days: int = 7, seed: int = 42) -> List[float]:
    """
    Return a deterministic synthetic time series for a metric.

    """
    random.seed(seed)
    based = 100.0
    return [based - i * random.uniform(0.5, 1.5) for i in range(days)]


def get_top_movers(seed: int = 42) -> Dict[str, float]:
    """
    Return deterministic synthetic top movers (category -> % change).
    """

    random.seed(seed)
    return {
        "Finance": -0.12,
        "Travel": -0.08,
        "Retail": 0.02,
    }