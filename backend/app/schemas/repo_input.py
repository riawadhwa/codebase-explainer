from pydantic import BaseModel, HttpUrl
from typing import Optional, Literal

class RepoInput(BaseModel):
    source_type: Literal["github", "zip"]
    repo_url: Optional[HttpUrl] = None
    max_files: int = 40
