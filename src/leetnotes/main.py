import typer

from .db import init_db, reset_db, add_problem, delete_problem, get_problems
from .models import Difficulty
from .output import ProblemsTable


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
def add(number: int, title: str, difficulty: Difficulty) -> None:
    problem_id = add_problem(number, title, difficulty)

    typer.echo(f"Added problem {number}.{title}")


@app.command()
def show() -> None:
    problems = get_problems()

    if not problems:
        typer.echo("No problems found.")
        return

    table = ProblemsTable()

    for problem in problems:
        table.add_problem(problem)

    table.show()




@app.command()
def delete(number: int, force: bool = False) -> None:
    if not force:
        typer.confirm(
            f"Delete problem #{number}?",
            abort=True,
        )

    deleted = delete_problem(number)

    if deleted:
        typer.echo(f"Problem {number} was deleted.")
    else:
        typer.echo(f"Problem {number} was not deleted.")


if __name__ == "__main__":
    app()