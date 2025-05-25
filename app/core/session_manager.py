# app/core/session_manager.py
import sqlite3
from datetime import datetime
from typing import List, Tuple
from app.core.config import Config

class SessionManager:
    """Сессии запросов в SQLite (путь из config.ini)."""

    def __init__(self, config_path: str = 'config.ini') -> None:
        cfg = Config(config_path)
        db_path = cfg.get('MEMORY', 'DB_PATH', fallback='sessions.db')
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
        cursor = self.conn.cursor()
        timestamp = datetime.now().isoformat()
        cursor.execute(
            'INSERT INTO sessions (timestamp, prompt, response) VALUES (?, ?, ?)',
            (timestamp, prompt, response)
        )
        self.conn.commit()

    def get_sessions(self) -> List[Tuple[int, str, str, str]]:
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM sessions')
        return cursor.fetchall()

    def __del__(self):
        self.conn.close()