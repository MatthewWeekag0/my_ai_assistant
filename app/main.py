# app/main.py
import sys
from PyQt5 import QtWidgets
from app.router import Router
from app.core.memory import Memory
from app.ui.mainwindow import MainWindow
from app.ui.tray_icon import TrayIcon
from app.adapters.websearch_adapter import WebSearchModule
from app.system_module import SystemModule
# from app.ilm.llm_module import LLMModule  # <- сюда подтягивайте ваш LLM

def main() -> None:
    """
    Точка входа: запускает GUI с тыреем и маршрутизатором.
    """
    app_qt = QtWidgets.QApplication(sys.argv)

    # Инициализация модулей
    memory = Memory()
    modules = {
        'search': WebSearchModule(),
        'system': SystemModule(),
        # 'clients': LLMModule(),
    }
    router = Router(modules)

    # GUI
    main_win = MainWindow(router)
    tray = TrayIcon(icon_path="path/to/icon.png", main_window=main_win)
    tray.show()
    sys.exit(app_qt.exec_())

if __name__ == "__main__":
    main()
