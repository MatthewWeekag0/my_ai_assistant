# ui/mainwindow.py
from PyQt5.QtWidgets import QMainWindow

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My AI Assistant")
        # Инициализация интерфейса
