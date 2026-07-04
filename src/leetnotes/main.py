import typer
import webbrowser

from .db import (
    init_db,
    reset_db,
    add_problem,
    delete_problem,
    get_problems,
    get_status,
    update_status,
    get_stats,
    get_slug,
)
from .models import Difficulty, Status
from .output import ProblemsTable, StatsTable
from .service import create_slug, return_url

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
def add(
    number: int, title: str, difficulty: Difficulty, status: Status = Status.TODO
) -> None:
    slug = create_slug(title)
    add_problem(number, title, difficulty, slug, status)

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
        typer.echo("Problem not found.")


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


@app.command()
def stats(stat_name: str) -> None:
    stats_data = get_stats(stat_name)

    for stat_name, values in stats_data.items():
        table = StatsTable(
            title=f"{stat_name.capitalize()} Stats",
            category_name=stat_name.capitalize(),
        )

        for name, quantity in values.items():
            table.add_stat(name, quantity)

        table.show()


@app.command()
def open(number: int) -> None:
    slug = get_slug(number)
    url = return_url(slug)

    if url:
        typer.echo(f"Opened {url}")
        webbrowser.open(url)
    else:
        typer.echo(f"There is no such problem #{number}")


if __name__ == "__main__":
    app()
