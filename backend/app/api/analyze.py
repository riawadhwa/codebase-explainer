from fastapi import APIRouter, HTTPException
from app.schemas.repo_input import RepoInput
from app.services.github_service import download_repo_zip
from app.services.repo_scanner import scan_repository

router = APIRouter(prefix="/analyze", tags=["analysis"])

@router.post("/")
def analyze_repo(payload: RepoInput):
    try:
        if payload.source_type == "github":
            repo_path = download_repo_zip(str(payload.repo_url))
        else:
            raise HTTPException(status_code=400, detail="ZIP upload not implemented yet")

        files = scan_repository(repo_path, payload.max_files)

        return {
            "status": "success",
            "file_count": len(files),
            "files": files
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
