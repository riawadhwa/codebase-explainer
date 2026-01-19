from pydantic import BaseModel
from typing import List

class ProjectSummary(BaseModel):
    project_type: str
    primary_language: str
    frameworks: List[str]
    entry_points: List[str]
