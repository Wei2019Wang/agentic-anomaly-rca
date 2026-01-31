from pydantic import BaseModel
from typing import Any, Optional


class Evidence(BaseModel):
    source: str            # tool name
    output: Any            # tool result
    citation: str          # human-readable reference
    success: bool = True
    error: Optional[str] = None
