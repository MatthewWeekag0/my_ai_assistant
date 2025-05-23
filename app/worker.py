# worker.py
from PyQt5.QtCore import QObject, QThread, pyqtSignal

class Worker(QObject):
    finished = pyqtSignal(str)
    error = pyqtSignal(str)

    def __init__(self, llm_client, prompt):
        super().__init__()
        self.llm_client = llm_client
        self.prompt = prompt

    def run(self):
        try:
            response = self.llm_client.get_response(self.prompt)
            self.finished.emit(response)
        except Exception as e:
            self.error.emit(str(e))
