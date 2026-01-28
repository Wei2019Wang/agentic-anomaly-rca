from typing import List
import statistics


def rolling_zscore(
    series: List[float],
    window: int = 5,
    threshold: float = 3.0,
) -> List[int]:
    """
    Return indices where rolling z-score exceeds threshold.
    """

    anomalies = []

    for i in range(window, len(series)):
        window_slice = series[i - window : i]
        mean = statistics.mean(window_slice)
        stdev = statistics.stdev(window_slice)

        if stdev == 0:
            continue

        z = abs((series[i] - mean) / stdev)
        if z > threshold:
            anomalies.append(i)

    return anomalies

def rolling_mad(
    series: List[float],
    window: int = 5,
    threshold: float = 4.0,
) -> List[int]:

    """
    Return indices where rolling MAD score exceeds threshold.
    """

    anomalies = []

    for i in range(window, len(series)):
        window_slice = series[i - window : i]
        median = statistics.median(window_slice)
        deviations = [abs(x - median) for x in window_slice]
        mad = statistics.median(deviations)

        if mad == 0:
            continue

        score = abs(series[i] - median) / mad
        
        if score > threshold:
            anomalies.append(i)

    return anomalies
        
