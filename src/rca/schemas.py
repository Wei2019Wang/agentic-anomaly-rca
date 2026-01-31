from typing import List, Dict, Any
from pydantic import BaseModel, Field   

class RCAExplanation(BaseModel):
    anomaly_id: int
    dimensions: List[str]
    explanation: str
    confidence: float


class RCAReport(BaseModel):
    alert_id: str
    explanations: List[RCAExplanation]
    

class Hypothesis(BaseModel):
    cause: str
    prior: float = Field(ge=0.0, le=1.0)
    required_evidence: List[str]
    score: float = Field(ge=0.0, le=1.0)

class ToolInvocation(BaseModel):
    tool_name: str
    args: Dict[str, Any]

    