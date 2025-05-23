# app/main.py

import sys
from app import router
from app import memory_module
from worker import Worker
from PyQt5.QtCore import QThread, pyqtSignal, QObject

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

def main():
    print("Добро пожаловать в My AI Assistant!")
    memory = memory_module.Memory()

    while True:
        try:
            user_input = input("Введите ваш запрос (или 'выход' для завершения): ")
            if user_input.lower() in ['выход', 'exit']:
                print("Завершение работы. До свидания!")
                break

            response = router.route_request(user_input, memory)
            print(f"Ответ: {response}")

        except KeyboardInterrupt:
            print("\nПрограмма прервана пользователем.")
            sys.exit(0)
        except Exception as e:
            print(f"Произошла ошибка: {e}")

def on_send(self):
    prompt = self.input_field.text()
    self.thread = QThread()
    self.worker = Worker(self.llm_client, prompt)
    self.worker.moveToThread(self.thread)
    self.thread.started.connect(self.worker.run)
    self.worker.finished.connect(self.display_response)
    self.worker.error.connect(self.display_error)
    self.worker.finished.connect(self.thread.quit)
    self.worker.finished.connect(self.worker.deleteLater)
    self.thread.finished.connect(self.thread.deleteLater)
    self.thread.start()

if __name__ == "__main__":
    main()
