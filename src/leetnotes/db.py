import sqlite3
from pathlib import Path

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
