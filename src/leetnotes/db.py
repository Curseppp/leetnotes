import sqlite3
from pathlib import Path
from typing import List

from .models import Difficulty, Problem, PublicProblem

DB_PATH = Path("leetnotes.db")



def get_connection() -> sqlite3.Connection:
    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return sqlite3.connect(DB_PATH)


def init_db():
    with get_connection() as conn:
        conn.execute("""
        CREATE TABLE IF NOT EXISTS problems
        (
           id INTEGER PRIMARY KEY AUTOINCREMENT,
            number INTEGER NOT NULL UNIQUE,
            title TEXT NOT NULL,
            slug TEXT NOT NULL,
            difficulty TEXT NOT NULL CHECK(difficulty IN ('easy', 'medium', 'hard')),
            status TEXT NOT NULL CHECK(status IN ('TODO', 'SOLVING', 'SOLVED', 'REVIEW')) DEFAULT 'TODO'    
        )
        """)


def reset_db() -> None:
    with get_connection() as conn:
        conn.execute("DROP TABLE IF EXISTS problems")

    init_db()


def delete_problem(number: int) -> bool:
    with get_connection() as conn:
        cursor = conn.execute(
            "DELETE FROM problems WHERE number = ?",
            (number,),
        )

        return cursor.rowcount > 0


def add_problem(number: int, title: str, difficulty: Difficulty) -> int:
    with get_connection() as conn:
        slug = f"{number}-{title}"
        cursor = conn.execute(
            """
            INSERT INTO problems (number, title, slug, difficulty)
            VALUES (?, ?, ?, ?)
            """,
            (number, title, slug, difficulty.value)
        )

        return cursor.lastrowid

def get_problems() -> List[PublicProblem]:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            SELECT number, title, difficulty, status FROM problems;
            """
        )

        problems = []
        for number, title, difficulty, status in cursor.fetchall():
            problems.append(PublicProblem(number, title, difficulty, status))

        return problems

