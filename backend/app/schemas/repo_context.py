from pydantic import BaseModel
from typing import List, Optional

class FileInfo(BaseModel):
    path: str

class RepoContext(BaseModel):
    file_tree: List[FileInfo]
    readme: Optional[str] = None
