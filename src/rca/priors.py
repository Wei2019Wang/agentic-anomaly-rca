from typing import Dict, List
from incident_memory.categories import INCIDENT_CATEGORIES

def initialize_prior() -> Dict[str, float]:
    """
        Start with uniform priors over all known root-cause categories.
    """
    n = len(INCIDENT_CATEGORIES)
    return {c: 1.0/n for c in INCIDENT_CATEGORIES}


def adjust_prior_with_memory(
    prior: Dict[str, float],
    retrieved_incidents: List[Dict],
    alpha: float = 0.5,
) -> Dict[str, float]:
    """
    Adjust priors using retrieved incidents.

    alpha controls how strongly memory influences the prior:
    - alpha = 0.0 → ignore memory
    - alpha = 1.0 → trust memory fully
    """

    if not retrieved_incidents:
        return prior

    # Cont causes in memory
    memory_counts = {k: 0 for k in prior.keys()}
    for inc in retrieved_incidents:
        memory_counts[inc["root_cause"]] += 1

    total = sum(memory_counts.values())
    memory_dist = {
        k: v /total if total > 0 else 0.0
        for k, v in memory_counts.items()
    }

    # Blend priors
    adjusted = {}
    for cause in prior.keys():
        adjusted[cause] = (1 - alpha) * prior[cause] + alpha * memory_dist.get(cause, 0.0)

    return adjusted