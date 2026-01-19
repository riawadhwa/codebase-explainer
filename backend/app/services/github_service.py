import requests
import zipfile
import tempfile
import os
import shutil
from urllib.parse import urlparse



def parse_github_url(repo_url: str):
    """
    Extract owner and repo name from GitHub URL
    """
    parsed = urlparse(repo_url)
    parts = parsed.path.strip("/").split("/")

    if len(parts) < 2:
        raise ValueError("Invalid GitHub repository URL")

    owner, repo = parts[0], parts[1]
    return owner, repo



def download_repo_zip(repo_url: str) -> str:
    owner, repo = parse_github_url(repo_url)

    default_branch = get_default_branch(owner, repo)
    zip_url = f"https://github.com/{owner}/{repo}/archive/refs/heads/{default_branch}.zip"

    response = requests.get(zip_url, stream=True)

    if response.status_code != 200:
        raise Exception(f"Failed to download repository ZIP for branch {default_branch}")

    temp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(temp_dir, "repo.zip")

    with open(zip_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)

    with zipfile.ZipFile(zip_path, "r") as zip_ref:
        zip_ref.extractall(temp_dir)

    extracted_path = None

    for item in os.listdir(temp_dir):
        full_path = os.path.join(temp_dir, item)
        if os.path.isdir(full_path):
            extracted_path = full_path
            break
    if not extracted_path:
        raise Exception("No extracted repository directory found")

    return extracted_path


def get_default_branch(owner: str, repo: str) -> str:
    api_url = f"https://api.github.com/repos/{owner}/{repo}"
    response = requests.get(api_url)

    if response.status_code != 200:
        raise Exception("Failed to fetch repository metadata")

    data = response.json()
    return data["default_branch"]
