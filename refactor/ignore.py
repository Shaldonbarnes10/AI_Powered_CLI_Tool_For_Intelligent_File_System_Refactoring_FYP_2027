from pathlib import Path
from fnmatch import fnmatch

def load_ignore_patterns():
    ignore_file = Path(".refactorignore")

    if not ignore_file.exists():
        print("Ignore file not found")
        return []

    with open(ignore_file) as f:
        return [
            line.strip()
            for line in f
            if line.strip() and not line.startswith("#")
        ]

def should_ignore(path: str, patterns: list[str]):

    for pattern in patterns:
        if fnmatch(path, pattern):
            return True

    return False       