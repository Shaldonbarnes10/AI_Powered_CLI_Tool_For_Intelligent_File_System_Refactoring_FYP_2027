from pathlib import Path

def print_tree(path: str, prefix: str = ""):
    base = Path(path)

    for i, item in enumerate(sorted(base.iterdir())):
        connector = "└── " if i == len(list(base.iterdir())) - 1 else "├── "
        print(prefix + connector + item.name)

        if item.is_dir():
            extension = "    " if i == len(list(base.iterdir())) - 1 else "│   "
            print_tree(str(item), prefix + extension)