from pathlib import Path

def get_metadata(file_path: Path):

    stat = file_path.stat()

    return {
        "name": file_path.name,
        "extension": file_path.suffix,
        "size": stat.st_size,
        "is_dir": file_path.is_dir(),
    }