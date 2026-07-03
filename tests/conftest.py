from typing import List

import pytest

from leetnotes.db import init_db
from leetnotes.models import Problem, Difficulty, Status
from leetnotes.db import add_problem


@pytest.fixture
def test_db(tmp_path, monkeypatch):
    db_path = tmp_path / "test.db"

    monkeypatch.setattr("leetnotes.db.DB_PATH", db_path)

    init_db()

    return db_path


@pytest.fixture
def sample_problems(test_db) -> List[Problem]:

    problems = [
        Problem(1, "Problem 1", "problem-1", Difficulty.EASY, Status.SOLVED),
        Problem(2, "Problem 2", "problem-2", Difficulty.MEDIUM, Status.SOLVING),
        Problem(3, "Problem 3", "problem-3", Difficulty.HARD, Status.TODO),
        Problem(4, "Problem 4", "problem-4", Difficulty.HARD, Status.REVIEW),
        Problem(5, "Problem 5", "problem-5", Difficulty.EASY, Status.SOLVED),
        Problem(6, "Problem 6", "problem-6", Difficulty.EASY, Status.SOLVED),
        Problem(7, "Problem 7", "problem-7", Difficulty.EASY, Status.SOLVED),
    ]

    for problem in problems:
        add_problem(
            problem.number,
            problem.title,
            problem.difficulty,
            problem.slug,
            problem.status,
        )

    return problems
