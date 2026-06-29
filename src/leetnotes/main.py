import typer

app = typer.Typer()

@app.command()
def add(title: str):
    print(f"New problem was added: {title}!")

@app.command()
def delete(title: str):
    print(f"Problem was deleted: {title}.")


if __name__ == "__main__":
    app()