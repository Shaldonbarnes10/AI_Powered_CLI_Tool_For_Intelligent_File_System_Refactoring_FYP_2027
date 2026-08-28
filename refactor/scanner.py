from pathlib import Path

from refactor.ignore import should_ignore


def scan_directory(path: str, ignore_patterns: list[str]):

    files = []

    for item in Path(path).rglob("*"):

        if should_ignore(item.name, ignore_patterns):
            continue

        files.append(item)

    return files