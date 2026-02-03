from typing import Dict, List, Optional, Any
from pydantic import BaseModel


# -------------------------
# Evidence
# -------------------------

class Evidence(BaseModel):
    source: str                 # tool name, e.g. "weather.get_events"
    output: Any                 # raw tool output
    citation: str               # human-readable reference
    success: bool = True
    error: Optional[str] = None


# -------------------------
# Hypothesis
# -------------------------

class Hypothesis(BaseModel):
    cause: str
    prior: float
    score: float
    required_evidence: List[str]

    # Day 13 addition
    supporting_evidence: List[Evidence] = []


class ToolInvocation(BaseModel):
    tool_name: str
    args: Dict[str, Any]




# -------------------------
# RCA Report (external API)
# -------------------------

class RCAExplanation(BaseModel):
    anomaly_id: int
    dimensions: List[str]
    explanation: str
    confidence: float


class RCAReport(BaseModel):
    alert_id: str
    explanations: List[RCAExplanation]

class CriticResult(BaseModel):
    hypothesis_id: str
    original_score: float
    revised_score: float
    supported: bool
    reason: str


class CriticOutput(BaseModel):
    results: List[CriticResult]
    should_retry: bool


# -------------------------
# RCA State (LangGraph State)
# -------------------------

class RCAState(BaseModel):
    # Input / trigger
    anomaly: str

    # Observation phase
    observations: Optional[str] = None

    # Memory / belief
    priors: Optional[Dict[str, float]] = None

    # Reasoning
    hypotheses: Optional[List[Hypothesis]] = None
    plan: Optional[List[Dict]] = None

    # Acting
    evidence: Optional[List[Evidence]] = None

    critic: CriticOutput | None = None
    # Output
    report: Optional[str] = None

    confidence: Optional[float] = None

    # Control
    retries: int = 0

    should_retry: bool = False
    
    max_retries: int = 2
