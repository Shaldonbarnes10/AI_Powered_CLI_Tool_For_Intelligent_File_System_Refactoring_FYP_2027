from pathlib import Path
import os


def validate_path(path: str):

    target = Path(path)

    if not target.exists():
        raise ValueError(f"Path does not exist: {path}")

    if not target.is_dir():
        raise ValueError(f"Not a directory: {path}")

    if not os.access(target, os.R_OK):
        raise ValueError(f"No read permission: {path}")

    return target