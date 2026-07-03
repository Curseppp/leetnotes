from leetnotes.db import add_problem, get_problem, get_problems, delete_problem
from leetnotes.models import Difficulty, Status


def test_add_problem(test_db):
    add_problem(1, "Two Sum", Difficulty.EASY, "two-slug")

    problem = get_problem(1)

    assert problem.number == 1
    assert problem.title == "Two Sum"
    assert problem.difficulty == Difficulty.EASY


def test_get_problems(sample_problems):
    problems = get_problems()
    hard_problems = get_problems(difficulty=Difficulty.HARD)
    solved_problems = get_problems(status=Status.SOLVED)

    assert len(problems) == len(sample_problems)
    assert len(hard_problems) == 2
    assert len(solved_problems) == 4


def test_get_problem(sample_problems):
    problem = get_problem(1)

    assert problem.number == 1
    assert problem.title == "Problem 1"
    assert problem.difficulty == Difficulty.EASY
    assert problem.status == Status.SOLVED


def test_delete_problem(sample_problems):
    assert len(get_problems()) == 7
    delete_problem(1)
    problems = get_problems()
    easy_problems = get_problems(difficulty=Difficulty.EASY)

    assert len(problems) == 6
    assert len(easy_problems) == 3
