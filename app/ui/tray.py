# ui/tray.py
from PyQt5.QtWidgets import QSystemTrayIcon

class TrayIcon(QSystemTrayIcon):
    def __init__(self, parent=None):
        super().__init__(parent)
        # Инициализация иконки