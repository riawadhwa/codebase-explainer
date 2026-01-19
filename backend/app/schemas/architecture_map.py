from pydantic import BaseModel
from typing import List, Dict

class ArchitectureMap(BaseModel):
    overview: str
    components: Dict[str, str]
    entry_points: List[str]
    run_commands: List[str]
    notes: List[str]
