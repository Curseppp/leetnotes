import typer
from rich.table import Table

from .db import init_db, reset_db, add_problem, delete_problem, get_problems
from .models import Difficulty, PublicProblem
from .console import console


app = typer.Typer()

def show_problems_table(problems: list[PublicProblem]) -> None:
    table = Table(title="LeetCode")

    table.add_column("№")
    table.add_column("Title")
    table.add_column("Difficulty")
    table.add_column("Status")

    for problem in problems:
        table.add_row(
            str(problem.number),
            problem.title,
            problem.difficulty,
            problem.status,
        )

    console.print(table)


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

    show_problems_table(problems)


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