# app/core/session_manager.py
import sqlite3
from datetime import datetime
from typing import List, Tuple

class SessionManager:
    """
    Сохраняет и извлекает сессии запросов в локальной SQLite-БД.
    """

    def __init__(self, db_path: str = 'sessions.db') -> None:
        self.conn = sqlite3.connect(db_path)
        self._create_table()

    def _create_table(self) -> None:
        cursor = self.conn.cursor()
        cursor.execute(
            '''
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                prompt TEXT,
                response TEXT
            )
            '''
        )
        self.conn.commit()

    def save_session(self, prompt: str, response: str) -> None:
        """
        Сохраняет новую сессию с отметкой времени.
        """
        cursor = self.conn.cursor()
        timestamp = datetime.now().isoformat()
        cursor.execute(
            'INSERT INTO sessions (timestamp, prompt, response) VALUES (?, ?, ?)',
            (timestamp, prompt, response)
        )
        self.conn.commit()

    def get_sessions(self) -> List[Tuple[int, str, str, str]]:
        """
        Возвращает все сохранённые сессии.
        """
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM sessions')
        return cursor.fetchall()
