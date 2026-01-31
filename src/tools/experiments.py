# src/tools/experiments.py

from typing import Dict


def get_active_experiments() -> Dict[str, str]:
    """
    Return fake experiment statuses.
    """
    return {
        "exp_search_ranking_v3": "ramped_down",
        "exp_ads_layout_test": "stable",
    }


# src/tools/experiments.py

def get_changes(experiment_id: str | None = None):
    """
    Mock experiment change lookup.
    """
    return {
        "experiment_id": experiment_id or "EXP_123",
        "change_type": "treatment_enabled",
        "impact": "negative",
        "metric": "RPM",
        "delta_pct": -8.5,
    }
