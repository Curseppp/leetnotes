from leetnotes.db import (
    add_problem,
    get_problem,
    get_problems,
    delete_problem,
    get_status,
    update_status,
    get_slug,
    get_stats,
)
from leetnotes.models import Difficulty, Status, StatsParam


def test_add_problem(test_db) -> None:
    add_problem(1, "Two Sum", Difficulty.EASY, "two-slug")

    problem = get_problem(1)

    assert problem.number == 1
    assert problem.title == "Two Sum"
    assert problem.difficulty == Difficulty.EASY
    assert problem.status == Status.TODO
    assert problem.slug == "two-slug"


def test_get_problems(sample_problems) -> None:
    problems = get_problems()
    hard_problems = get_problems(difficulty=Difficulty.HARD)
    solved_problems = get_problems(status=Status.SOLVED)

    assert len(problems) == len(sample_problems)
    assert len(hard_problems) == 2
    assert len(solved_problems) == 4


def test_get_problem(sample_problems) -> None:
    problem = get_problem(1)

    assert problem.number == 1
    assert problem.title == "Problem 1"
    assert problem.difficulty == Difficulty.EASY
    assert problem.status == Status.SOLVED


def test_delete_problem(sample_problems) -> None:
    assert len(get_problems()) == 7

    delete_problem(1)
    problems = get_problems()
    easy_problems = get_problems(difficulty=Difficulty.EASY)

    assert len(problems) == 6
    assert len(easy_problems) == 3


def test_get_status(sample_problems) -> None:
    status = get_status(4)

    assert status == Status.REVIEW


def test_update_status(sample_problems) -> None:
    update_status(2, Status.SOLVED)
    new_status = get_status(2)

    assert new_status == Status.SOLVED


def test_get_slug(sample_problems) -> None:
    slug = get_slug(7)

    assert slug == "problem-7"


def test_get_stats(sample_problems) -> None:
    stats_by_diff = get_stats(StatsParam.DIFFICULTY)
    stats_by_status = get_stats(StatsParam.STATUS)

    assert {"difficulty": {"easy": 4, "medium": 1, "hard": 2}} == stats_by_diff
    assert {
        "status": {"todo": 1, "solving": 1, "solved": 4, "review": 1}
    } == stats_by_status
