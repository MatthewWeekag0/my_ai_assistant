# app/worker.py
from PyQt5.QtCore import QObject, pyqtSignal
from typing import Any

class Worker(QObject):
    """
    Фоновый поток для обращения к LLM-клиенту без блокировки UI.
    """
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, llm_client: Any, prompt: str) -> None:
        super().__init__()
        self.llm_client = llm_client
        self.prompt = prompt

    def run(self) -> None:
        try:
            resp = self.llm_client.get_response(self.prompt)
            self.finished.emit(resp)
        except Exception as e:
            self.error.emit(str(e))
