import json
from fastapi import APIRouter, HTTPException
from app.schemas.repo_input import RepoInput
from app.services.github_service import download_repo_zip
from app.schemas.repo_context import RepoContext, FileInfo
from app.agents.project_classifier import get_project_classifier
from app.schemas.project_summary import ProjectSummary
from app.services.repo_scanner import (
    scan_repository,
    extract_readme,
    compute_repo_stats,
    extract_package_json,
)
from app.agents.architecture_mapper import get_architecture_agent
from app.schemas.architecture_map import ArchitectureMap


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

        package_json = extract_package_json(repo_path)
        stats = compute_repo_stats(files)


        classifier_agent = get_project_classifier()
        architecture_agent = get_architecture_agent()

        agent_input = f"""
        REPOSITORY STATISTICS:
        {json.dumps(stats, indent=2)}

        PACKAGE.JSON CONTENT:
        {json.dumps(package_json, indent=2) if package_json else "NO PACKAGE.JSON"}

        FILE PATHS:
        {json.dumps([f.path for f in context.file_tree], indent=2)}

        README CONTENT:
        {context.readme if context.readme else "NO README"}
        """

        agent_result = classifier_agent.run_sync(agent_input)
        architecture_result = architecture_agent.run_sync(agent_input)

        raw_text = agent_result.output
        raw_arch = architecture_result.output.strip()

        try:
            parsed = json.loads(raw_text)
            summary = ProjectSummary.model_validate(parsed)
            architecture = ArchitectureMap.model_validate_json(raw_arch)

        except Exception as e:
            raise HTTPException(
                status_code=500,
                detail=f"Failed to parse agent output: {str(e)}"
            )

        return {
            "status": "success",
            "repo_summary": summary.model_dump(),
            "architecture": architecture.model_dump()
        }
            

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
