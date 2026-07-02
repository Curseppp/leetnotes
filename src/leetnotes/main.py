import typer

from .db import init_db, reset_db, add_problem, delete_problem, get_problems, get_status, update_status
from .models import Difficulty, Status
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
def status(number: int) -> None:
    problem_status = get_status(number)

    if problem_status is None:
        typer.echo(f"Problem #{number} not found.")
        return

    typer.echo(f"Problem #{number}: {problem_status.value}")


@app.command()
def edit_status(number: int, status: Status) -> None:
    res = update_status(number, status)

    if res:
        typer.echo(f"Changed status for problem #{number}.")
    else:
        typer.echo(f"Problem not found.")



@app.command()
def show(difficulty: Difficulty | None = None, status: Status | None = None) -> None:
    problems = get_problems(difficulty, status)

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