# app/main.py
import sys
from PyQt5 import QtWidgets

from app.core.memory import Memory
from app.core.router import Router
from app.clients.llm_client import LLMClient
from app.adapters.websearch_adapter import WebSearchAdapter
from app.adapters.telegram_adapter import TelegramAdapter
from app.adapters.voice_adapter import VoiceAdapter
from app.adapters.word_adapter import WordAdapter
from app.core.system_service import SystemService
from app.modules.file_module import FileModule
from app.modules.browser_module import BrowserModule
from app.modules.worker import Worker
from app.ui.mainwindow import MainWindow
from app.ui.tray_icon import TrayIcon
# При необходимости добавьте: LLMClient, другие адаптеры, модули и сервисы


def main() -> None:
    app_qt = QtWidgets.QApplication(sys.argv)

    # Инициализация основных компонентов
    memory = Memory()
    llm = LLMClient()
    router = Router({
        'llm': llm,
        'search': WebSearchAdapter(),
        'telegram': TelegramAdapter(token="YOUR_TOKEN"),
        'voice': VoiceAdapter(),
        'word': WordAdapter(),
        'system': SystemService(),
        'file': FileModule(),
        'browser': BrowserModule(),
    })

    # GUI с треем
    main_win = MainWindow(router)
    tray = TrayIcon(icon_path="path/to/icon.png", main_window=main_win)
    tray.show()

    sys.exit(app_qt.exec_())


if __name__ == "__main__":
    main()