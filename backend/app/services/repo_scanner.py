import os
from app.utils.file_filters import IGNORE_DIRS, ALLOWED_EXTENSIONS

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
