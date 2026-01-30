"""
Canonical incident root-cause categories.

These categories are intentionally coarse and stable.
They are used for:
- historical incident memory
- hypothesis priors
- evaluation labels
"""

INCIDENT_CATEGORIES = [
    "Weather",
    "AdvertiserPullback",
    "ExperimentChange",
    "InfraLatency",
    "DataPipelineIssue",
]
