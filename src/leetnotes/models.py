from dataclasses import dataclass
from enum import Enum


class Difficulty(str, Enum):
    EASY = "easy"
    MEDIUM = "medium"
    HARD = "hard"


class Status(str, Enum):
    TODO = "todo"
    SOLVING = "solving"
    SOLVED = "solved"
    REVIEW = "review"


@dataclass
class Problem:
    number: int
    title: str
    url: str
    difficulty: Difficulty
    status: Status


@dataclass
class PublicProblem:
    number: int
    title: str
    difficulty: Difficulty
    status: Status
    url: str

