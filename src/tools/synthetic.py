import random


def generate_metric_series(seed: int = 42):
    random.seed(seed)
    return [100 - i * random.uniform(0.8, 1.2) for i in range(7)]