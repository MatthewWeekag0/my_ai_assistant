# app/gui.py
from PyQt5 import QtWidgets
from typing import Any

class MainWindow(QtWidgets.QMainWindow):
    """
    Встроенный GUI-интерфейс без трея.
    """

    def __init__(self, router: Any) -> None:
        super().__init__()
        self.router = router
        self.setWindowTitle("ИИ-ассистент")
        self.resize(500, 600)

        self.chat = QtWidgets.QTextEdit(self)
        self.chat.setReadOnly(True)
        self.input = QtWidgets.QLineEdit(self)
        self.input.setPlaceholderText("Введите запрос...")
        self.send_btn = QtWidgets.QPushButton("Отправить", self)
        self.send_btn.clicked.connect(self.handle_send)

        vbox = QtWidgets.QVBoxLayout()
        vbox.addWidget(self.chat)
        hbox = QtWidgets.QHBoxLayout()
        hbox.addWidget(self.input)
        hbox.addWidget(self.send_btn)
        vbox.addLayout(hbox)

        container = QtWidgets.QWidget()
        container.setLayout(vbox)
        self.setCentralWidget(container)

    def handle_send(self) -> None:
        text = self.input.text().strip()
        if not text:
            return
        self.chat.append(f"Вы: {text}")
        self.input.clear()
        resp = self.router.handle_request(text)
        self.chat.append(f"Ассистент: {resp}")
