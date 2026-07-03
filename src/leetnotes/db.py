import sqlite3
from pathlib import Path
from typing import Literal

from .models import Difficulty, PublicProblem, Status
from .service import create_slug


DB_PATH = Path.home() / ".leetnotes" / "leetnotes.db"

StatsParam = Literal["difficulty", "status"]



def get_connection() -> sqlite3.Connection:
    DB_PATH.parent.mkdir(parents=True, exist_ok=True)

    conn = sqlite3.connect(DB_PATH)
    conn.row_factory = sqlite3.Row
    return conn


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
            status TEXT NOT NULL CHECK(status IN ('todo', 'solving', 'solved', 'review')) DEFAULT 'todo'    
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


def add_problem(
        number: int,
        title: str,
        difficulty: Difficulty,
        slug: str,
        status: Status | None = Status.TODO,
) -> int:
    with get_connection() as conn:
        cursor = conn.execute(
            """
            INSERT INTO problems (number, title, slug, difficulty, status)
            VALUES (?, ?, ?, ?, ?)
            """,
            (number, title, slug, difficulty.value, status.value),
        )

        return cursor.lastrowid


def get_status(number: int) -> Status | None:
    with get_connection() as conn:
        cursor = conn.execute(
            " SELECT status FROM problems WHERE number = ?",
            (number, ),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return Status(row["status"])


def update_status(number: int, status: Status):
    with get_connection() as conn:
        cursor = conn.execute(
            "UPDATE problems SET status = ? WHERE number = ?",
            (status.value, number,),
        )

        return cursor.rowcount



def get_problems(
    difficulty: Difficulty | None = None,
    status: Status | None = None,
) -> list[PublicProblem]:
    query = """
        SELECT number, title, difficulty, status
        FROM problems
    """

    conditions = []
    params = []

    if difficulty is not None:
        conditions.append("difficulty = ?")
        params.append(difficulty.value)

    if status is not None:
        conditions.append("status = ?")
        params.append(status.value)

    if conditions:
        query += " WHERE " + " AND ".join(conditions)

    query += " ORDER BY number"

    with get_connection() as conn:
        cursor = conn.execute(query, params)
        rows = cursor.fetchall()

        return [
            PublicProblem(
                number=row["number"],
                title=row["title"],
                difficulty=Difficulty(row["difficulty"]),
                status=Status(row["status"]),
            )
            for row in rows
        ]

def get_slug(number: int) -> str | None:
    with get_connection() as conn:
        cursor = conn.execute(
            " SELECT slug FROM problems WHERE number = ?",
            (number, ),
        )

        row = cursor.fetchone()

        if row is None:
            return None

        return str(row["slug"])

def get_stats(param: StatsParam) -> dict[str, dict[str, int]]:
    allowed_params = {"difficulty", "status"}

    if param not in allowed_params:
        raise ValueError(f"Invalid stats param: {param}")

    with get_connection() as conn:
        cursor = conn.execute(
            f"""
            SELECT {param}, COUNT(*) AS count
            FROM problems
            GROUP BY {param}
            """
        )

        return {
            param: {
                row[param]: row["count"]
                for row in cursor.fetchall()
            }
        }
