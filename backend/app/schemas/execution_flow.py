from pydantic import BaseModel
from typing import List

class ExecutionFlow(BaseModel):
    summary: str
    steps: List[str]
    notes: List[str]
