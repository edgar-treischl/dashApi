# dashApi/cli.py

import typer

app = typer.Typer()

@app.command()
def hello(name: str):
    """
    Simple CLI command that greets the user by name.
    """
    print(f"Hello, {name}!")

if __name__ == "__main__":
    app()
