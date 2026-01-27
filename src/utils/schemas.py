from typing import TypedDict, List, Optional


class RCAState(TypedDict):
    """
    Global state passed through the LangGraph.
    """

    # Raw anomaly description (input)
    anomaly: str

    # Initial observations produced by the observer agent
    observations: Optional[str]

    # Candidate root-cause hypotheses with priors
    hypotheses: Optional[List["Hypothesis"]]

    # Evidence collected for each hypothesis
    evidence: Optional[List["Evidence"]]

    # Final confidence score after critique (0–1)
    confidence: Optional[float]

    # Number of retries performed by the graph
    retries: int


class Hypothesis(TypedDict):
    """
    Candidate explanation for an anomaly.
    """

    # Human-readable cause (e.g., "Demand pullback")
    cause: str

    # Prior belief before evidence is collected (0–1)
    prior: float


class Evidence(TypedDict):
    """
    Evidence supporting or refuting a hypothesis.
    """

    # Hypothesis this evidence refers to
    hypothesis: str

    # Description of the signal (metric, log, config)
    signal: str

    # Strength of support or refutation (0–1)
    strength: float
