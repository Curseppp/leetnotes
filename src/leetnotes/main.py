import typer
from .db import get_connection, init_db, reset_db
from .models import Difficulty

app = typer.Typer()

@app.callback()
def main() -> None:
    init_db()


@app.command()
def init() -> None:
    init_db()
    typer.echo("Database initialized.")

@app.command()
def reset() -> None:
    reset_db()
    typer.echo("Database was reset.")


@app.command()
def add_problem(number: int, title: str, difficulty: Difficulty) -> int:
    with get_connection() as conn:
        slug = f"{number}-{title}"
        cursor = conn.execute(
            """
            INSERT INTO problems (number, title, slug, difficulty)
            VALUES (?, ?, ?, ?)
            """,
            (number, title, slug, difficulty.value)
        )

        return cursor.lastrowid


@app.command()
def add(title: str):
    print(f"New problem was added: {title}!")


@app.command()
def delete(title: str):
    print(f"Problem was deleted: {title}.")


if __name__ == "__main__":
    app()