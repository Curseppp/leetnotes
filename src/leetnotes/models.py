from dataclasses import dataclass
from datetime import datetime
from enum import Enum

class Difficulty(Enum):
    easy = "easy"
    medium = "medium"
    hard = "hard"


class Status(Enum):
    TODO = 0
    SOLVING = 1
    SOLVED = 2
    REVIEW = 3


@dataclass
class Problem:
    number: int
    title: str
    slug: str
    difficulty: Difficulty
    status: Status
