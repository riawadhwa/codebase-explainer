import json
from fastapi import APIRouter, HTTPException
from app.schemas.repo_input import RepoInput
from app.services.github_service import download_repo_zip
from app.services.repo_scanner import scan_repository
from app.schemas.repo_context import RepoContext, FileInfo
from app.services.repo_scanner import extract_readme
from app.agents.project_classifier import get_project_classifier
from app.schemas.project_summary import ProjectSummary
from app.services.repo_scanner import compute_repo_stats

router = APIRouter(prefix="/analyze", tags=["analysis"])

@router.post("/")
def analyze_repo(payload: RepoInput):
    try:
        if payload.source_type == "github":
            repo_path = download_repo_zip(str(payload.repo_url))
        else:
            raise HTTPException(status_code=400, detail="ZIP upload not implemented yet")
        
        readme = extract_readme(repo_path)
        files = scan_repository(repo_path, payload.max_files)

        context = RepoContext(
            file_tree=[FileInfo(path=f["path"]) for f in files],
            readme=readme
        )
        
        stats = compute_repo_stats(files)
        print("DEBUG — REPO STATS:")
        print(stats)

        classifier_agent = get_project_classifier()
        agent_input = f"""
        REPOSITORY STATISTICS:
        {json.dumps(stats, indent=2)}

        FILE PATHS:
        {json.dumps([f.path for f in context.file_tree], indent=2)}

        README CONTENT:
        {context.readme if context.readme else "NO README"}
        """

        agent_result = classifier_agent.run_sync(agent_input)


        print("AGENT RESPONSE TYPE:", type(agent_result))
        print("AGENT RESPONSE VALUE:")
        print(agent_result)
        raw_text = agent_result.output

        print("RAW MODEL OUTPUT:")
        print(raw_text)

        try:
            parsed = json.loads(raw_text)
            summary = ProjectSummary.model_validate(parsed)
        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to parse agent output: {str(e)}"
            )

        return {
            "status": "success",
            "repo_summary": summary.model_dump()
        }
            

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
