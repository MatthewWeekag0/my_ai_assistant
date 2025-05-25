# app/memory.py
import sqlite3
from typing import List, Tuple

class Memory:
    """
    Краткосрочная память диалога + сохранение в SQLite.
    """

    def __init__(self, db_path: str = 'memory.db') -> None:
        self.conn = sqlite3.connect(db_path)
        self._create_table()
        self.history: List[Tuple[str, str]] = []

    def _create_table(self) -> None:
        cur = self.conn.cursor()
        cur.execute(
            '''
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY,
                user_input TEXT,
                assistant_response TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
            '''
        )
        self.conn.commit()

    def add_interaction(self, user_input: str, response: str) -> None:
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO history (user_input, assistant_response) VALUES (?, ?)",
            (user_input, response)
        )
        self.conn.commit()
        self.history.append((user_input, response))

    def get_context(self, n: int = 5) -> List[Tuple[str, str]]:
        return self.history[-n:]
