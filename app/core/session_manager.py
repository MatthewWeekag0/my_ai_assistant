# core/session_manager.py
import sqlite3
from datetime import datetime

class SessionManager:
    def __init__(self, db_path='sessions.db'):
        self.conn = sqlite3.connect(db_path)
        self.create_table()

    def create_table(self):
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS sessions (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                timestamp TEXT,
                prompt TEXT,
                response TEXT
            )
        ''')
        self.conn.commit()

    def save_session(self, prompt, response):
        cursor = self.conn.cursor()
        timestamp = datetime.now().isoformat()
        cursor.execute('INSERT INTO sessions (timestamp, prompt, response) VALUES (?, ?, ?)', (timestamp, prompt, response))
        self.conn.commit()

    def get_sessions(self):
        cursor = self.conn.cursor()
        cursor.execute('SELECT * FROM sessions')
        return cursor.fetchall()
