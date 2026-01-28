import random
from typing import List


def generate_series_with_anomalies(
    length: int = 100,
    num_anomalies: int = 10,
    seed: int = 42,
) -> List[float]:
    """
    Generate synthetic time series with injected anomalies.
    """

    series = [100 + random.uniform(-1, 1) for _ in range(length)]

    anomaly_indices = random.sample(range(length), num_anomalies)

    for idx in anomaly_indices:
        series[idx] += random.choice([-20, 20])
    print(f"Anomaly indices: {anomaly_indices}")
    return series
