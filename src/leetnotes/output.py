from rich.table import Table

from .console import console
from .models import PublicProblem, Difficulty, Status


class ProblemsTable:
    def __init__(self) -> None:
        self.table = Table(title="LeetCode")

        self.table.add_column("№", style="cyan")
        self.table.add_column("Title", style="bold")
        self.table.add_column("Difficulty")
        self.table.add_column("Status")

    def add_problem(self, problem: PublicProblem) -> None:
        self.table.add_row(
            str(problem.number),
            problem.title,
            self._format_difficulty(problem.difficulty),
            self._format_status(problem.status),
        )

    def show(self) -> None:
        console.print(self.table)

    def _format_difficulty(self, difficulty: Difficulty) -> str:
        match difficulty:
            case Difficulty.easy:
                return "[green]easy[/green]"
            case Difficulty.medium:
                return "[yellow]medium[/yellow]"
            case Difficulty.hard:
                return "[red]hard[/red]"

    def _format_status(self, status: Status) -> str:
        match status:
            case Status.TODO:
                return "[dim]TODO[/dim]"
            case Status.SOLVING:
                return "[yellow]SOLVING[/yellow]"
            case Status.SOLVED:
                return "[green]SOLVED[/green]"
            case Status.REVIEW:
                return "[blue]REVIEW[/blue]"