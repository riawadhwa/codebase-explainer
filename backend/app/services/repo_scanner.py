import os
from app.utils.file_filters import IGNORE_DIRS, ALLOWED_EXTENSIONS
from collections import Counter


def scan_repository(repo_path: str, max_files: int = 40):
    collected_files = []

    for root, dirs, files in os.walk(repo_path):
        # modify dirs in-place to skip ignored folders
        dirs[:] = [d for d in dirs if d not in IGNORE_DIRS]

        for file in files:
            if len(collected_files) >= max_files:
                return collected_files

            _, ext = os.path.splitext(file)
            if ext.lower() not in ALLOWED_EXTENSIONS:
                continue

            full_path = os.path.join(root, file)
            relative_path = os.path.relpath(full_path, repo_path)

            collected_files.append({
                "path": relative_path,
                "absolute_path": full_path
            })

    return collected_files

def extract_readme(repo_path: str) -> str | None:
    for filename in os.listdir(repo_path):
        if filename.lower().startswith("readme"):
            readme_path = os.path.join(repo_path, filename)
            try:
                with open(readme_path, "r", encoding="utf-8", errors="ignore") as f:
                    return f.read()[:4000]  # cap size
            except Exception:
                return None
    return None




def compute_repo_stats(files):
    extensions = []
    filenames = []

    for f in files:
        _, ext = os.path.splitext(f["path"])
        if ext:
            extensions.append(ext.lower())
        filenames.append(os.path.basename(f["path"]))

    return {
        "total_files": len(files),
        "extension_counts": dict(Counter(extensions)),
        "common_filenames": list(set(filenames))[:20],
    }