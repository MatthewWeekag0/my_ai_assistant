# app/memory_module.py

import sqlite3

class MemoryModule:
    def __init__(self):
        self.conn = sqlite3.connect('memory.db')
        cur = self.conn.cursor()
        cur.execute('''
            CREATE TABLE IF NOT EXISTS history (
                id INTEGER PRIMARY KEY,
                user_input TEXT,
                assistant_response TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def save(self, user_input, assistant_response):
        cur = self.conn.cursor()
        cur.execute(
            "INSERT INTO history (user_input, assistant_response) VALUES (?, ?)",
            (user_input, assistant_response)
        )
        self.conn.commit()

class Memory:
    def __init__(self):
        self.history = []

    def add_interaction(self, user_input, response):
        self.history.append((user_input, response))

    def get_context(self, n=5):
        return self.history[-n:]
