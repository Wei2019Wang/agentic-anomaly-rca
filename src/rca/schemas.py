from typing import List
from pydantic import BaseModel

class RCAExplanation(BaseModel):
    anomaly_id: int
    dimensions: List[str]
    explanation: str
    confidence: float


class RCAReport(BaseModel):
    alert_id: str
    explanations: List[RCAExplanation]
    