from typing import List, Optional, Dict
from pydantic import BaseModel, Field


class RCAState(BaseModel):
    """
    Global state passed through the LangGraph.
    """

    # Raw anomaly description (input)
    anomaly: str

    # Initial observations produced by the observer agent
    observations: Optional[str] = None

    # Prior probabilities for hypotheses (dict mapping cause -> prior probability)
    priors: Optional[Dict[str, float]] = None

    # Candidate root-cause hypotheses with priors
    hypotheses: Optional[List["Hypothesis"]] = None

    # Evidence collection plan (List of ToolInvocation from rca.schemas)
    plan: Optional[List] = None

    # Evidence collected for each hypothesis
    evidence: Optional[List["Evidence"]] = None

    # Final confidence score after critique (0–1)
    confidence: Optional[float] = None
    
    report: Optional[str] = None
    # Number of retries performed by the graph
    retries: int = 0


class Hypothesis(BaseModel):
    """
    Candidate explanation for an anomaly.
    """

    # Human-readable cause (e.g., "Demand pullback")
    cause: str

    # Prior belief before evidence is collected (0–1)
    prior: float = Field(ge=0.0, le=1.0)


class Evidence(BaseModel):
    """
    Evidence supporting or refuting a hypothesis.
    """

    # Hypothesis this evidence refers to
    hypothesis: str

    # Description of the signal (metric, log, config)
    signal: str

    # Strength of support or refutation (0–1)
    strength: float = Field(ge=0.0, le=1.0)
