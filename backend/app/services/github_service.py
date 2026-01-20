import requests
import zipfile
import tempfile
import os
from urllib.parse import urlparse


GITHUB_API_BASE = "https://api.github.com"


def _github_headers():
    token = os.getenv("GITHUB_TOKEN")

    if not token:
        raise Exception("GITHUB_TOKEN is not set in environment variables")

    return {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "User-Agent": "RepoLens-AI"
    }


def parse_github_url(repo_url: str):
    parsed = urlparse(repo_url)
    parts = parsed.path.strip("/").split("/")

    if len(parts) < 2:
        raise ValueError("Invalid GitHub repository URL")

    owner, repo = parts[0], parts[1]
    return owner, repo


def get_default_branch(owner: str, repo: str) -> str:
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"

    response = requests.get(url, headers=_github_headers(), timeout=15)

    if response.status_code != 200:
        raise Exception(
            f"Failed to fetch repository metadata: {response.status_code} {response.text}"
        )

    return response.json()["default_branch"]


def download_repo_zip(repo_url: str) -> str:
    owner, repo = parse_github_url(repo_url)
    branch = get_default_branch(owner, repo)

    zip_url = f"https://github.com/{owner}/{repo}/archive/refs/heads/{branch}.zip"

    response = requests.get(
        zip_url,
        headers=_github_headers(),
        stream=True,
        timeout=30
    )

    if response.status_code != 200:
        raise Exception(
            f"Failed to download repository ZIP: {response.status_code}"
        )

    temp_dir = tempfile.mkdtemp()
    zip_path = os.path.join(temp_dir, "repo.zip")

    with open(zip_path, "wb") as f:
        for chunk in response.iter_content(chunk_size=8192):
            if chunk:
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
