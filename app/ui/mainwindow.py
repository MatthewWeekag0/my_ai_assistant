# app/ui/mainwindow.py
from PyQt5.QtWidgets import (
    QMainWindow, QTextEdit, QLineEdit,
    QPushButton, QVBoxLayout, QHBoxLayout, QWidget
)
from typing import Any

class MainWindow(QMainWindow):
    """
    Главное окно GUI для My AI Assistant.
    """

    def __init__(self, router: Any) -> None:
        super().__init__()
        self.router = router
        self.setWindowTitle("My AI Assistant")
        self.resize(600, 400)

        # Виджеты
        self.chat_history = QTextEdit(self)
        self.chat_history.setReadOnly(True)

        self.input_field = QLineEdit(self)
        self.input_field.setPlaceholderText("Введите ваш запрос...")

        self.send_button = QPushButton("Отправить", self)
        self.send_button.clicked.connect(self.handle_send)

        # Layout
        main_layout = QVBoxLayout()
        main_layout.addWidget(self.chat_history)

        bottom_layout = QHBoxLayout()
        bottom_layout.addWidget(self.input_field)
        bottom_layout.addWidget(self.send_button)
        main_layout.addLayout(bottom_layout)

        container = QWidget()
        container.setLayout(main_layout)
        self.setCentralWidget(container)

    def handle_send(self) -> None:
        """
        Отправка запроса из GUI и отображение ответа.
        """
        user_text = self.input_field.text().strip()
        if not user_text:
            return

        self.chat_history.append(f"Вы: {user_text}")
        self.input_field.clear()

        response = self.router.handle_request(user_text)
        self.chat_history.append(f"Ассистент: {response}")
