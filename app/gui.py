# app/gui.py

from PyQt5 import QtWidgets

class MainWindow(QtWidgets.QMainWindow):
    def __init__(self, router):
        super().__init__()
        self.router = router
        self.setWindowTitle("ИИ-ассистент")
        self.resize(500, 600)

        self.chat_history = QtWidgets.QTextEdit(self)
        self.chat_history.setReadOnly(True)

        self.input_field = QtWidgets.QLineEdit(self)
        self.input_field.setPlaceholderText("Введите ваш запрос...")

        self.send_button = QtWidgets.QPushButton("Отправить")
        self.send_button.clicked.connect(self.handle_send)

        layout = QtWidgets.QVBoxLayout()
        layout.addWidget(self.chat_history)

        h_layout = QtWidgets.QHBoxLayout()
        h_layout.addWidget(self.input_field)
        h_layout.addWidget(self.send_button)

        layout.addLayout(h_layout)

        central_widget = QtWidgets.QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

    def handle_send(self):
        user_text = self.input_field.text()
        if user_text:
            self.chat_history.append(f"<b>Вы:</b> {user_text}")
            self.input_field.clear()
            response = self.router.handle_request(user_text)
            self.chat_history.append(f"<b>Ассистент:</b> {response}")
