from rich.table import Table

from .console import console
from .models import PublicProblem, Difficulty, Status


class ProblemsTable:
    def __init__(self) -> None:
        self.table = Table(title="Leetnotes")

        self.table.add_column("№", style="cyan")
        self.table.add_column("Title", style="bold")
        self.table.add_column("Difficulty")
        self.table.add_column("Status")

    def add_problem(self, problem: PublicProblem) -> None:
        self.table.add_row(
            str(problem.number),
            problem.title,
            self._format_difficulty(problem.difficulty),
            self._format_status(problem.status)
        )

    def show(self) -> None:
        console.print(self.table)

    def _format_difficulty(self, difficulty: Difficulty) -> str:
        match difficulty:
            case Difficulty.EASY:
                return f"[green]{Difficulty.EASY.value}[/green]"
            case Difficulty.MEDIUM:
                return f"[yellow]{Difficulty.MEDIUM.value}[/yellow]"
            case Difficulty.HARD:
                return f"[red]{Difficulty.HARD.value}[/red]"


    def _format_status(self, status: Status) -> str:
        match status:
            case Status.TODO:
                return f"[dim]{Status.TODO.value.upper()}[/dim]"
            case Status.SOLVING:
                return f"[yellow]{Status.SOLVING.value.upper()}[/yellow]"
            case Status.SOLVED:
                return f"[green]{Status.SOLVED.value.upper()}[/green]"
            case Status.REVIEW:
                return f"[blue]{Status.REVIEW.value.upper()}[/blue]"


class StatsTable:
    def __init__(self, title: str, category_name: str) -> None:
        self.table = Table(title=title)

        self.table.add_column(category_name)
        self.table.add_column("Quantity", justify="right")

    def add_stat(self, name: str, quantity: int) -> None:
        self.table.add_row(name, str(quantity))

    def show(self) -> None:
        console.print(self.table)