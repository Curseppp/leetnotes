from dataclasses import dataclass
from enum import Enum

class Difficulty(Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"


class Status(Enum):
    TODO = "todo"
    SOLVING = "solving"
    SOLVED = "solved"
    REVIEW = "review"


@dataclass
class Problem:
    number: int
    title: str
    slug: str
    difficulty: Difficulty
    status: Status


@dataclass
class PublicProblem:
    number: int
    title: str
    difficulty: Difficulty
    status: Status

