import typer
from refactor.tree import print_tree
from importlib.metadata import version as get_version
from refactor.validation import validate_path
from refactor.scanner import scan_directory
from refactor.metadata import get_metadata
from refactor.ignore import load_ignore_patterns

app = typer.Typer(no_args_is_help=True)

@app.command()
def version():
    """Print version information"""
    print(get_version("refactor-cli"))

# @app.command()
# def tree(path: str = "."):
#     """Print folder structure"""
#     print_tree(path)

if __name__ == "__main__":
    app()

# validates folder
@app.command()
def tree(path: str = "."):
    """Display folder structure of given path"""
    try:
        validate_path(path)
        print_tree(path)

    except ValueError as e:
        typer.echo(f"Error: {e}")
        raise typer.Exit(code=1) 

# scanner
# files = scan_directory(".")
# print(len(files))    

@app.command()
def scan(path: str = "."):
    """Scan directory and display metadata"""

    try:
        validate_path(path)

        patterns = load_ignore_patterns()

        items = scan_directory(path, patterns)

        for item in items:
            print(get_metadata(item))

    except ValueError as e:
        typer.echo(f"Error: {e}")
        raise typer.Exit(code=1)  