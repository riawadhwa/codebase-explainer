from fastapi import APIRouter
from app.schemas.repo_input import RepoInput

router = APIRouter(prefix="/analyze", tags=["analysis"])

@router.post("/")
def analyze_repo(payload: RepoInput):
    return {
        "message": "Received input",
        "data": payload.dict()
    }
