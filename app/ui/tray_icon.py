# app/ui/tray_icon.py
from PyQt5.QtWidgets import QSystemTrayIcon, QMenu, QAction, QApplication
from PyQt5.QtGui import QIcon
from typing import Optional

class TrayIcon(QSystemTrayIcon):
    """
    Иконка в системном трее для управления приложением.
    """

    def __init__(self, icon_path: str, main_window: Optional[QApplication] = None) -> None:
        super().__init__(QIcon(icon_path))
        self.main_window = main_window
        self.setToolTip("My AI Assistant")

        # Контекстное меню
        menu = QMenu()
        open_act = QAction("Открыть")
        open_act.triggered.connect(self._show)
        exit_act = QAction("Выход")
        exit_act.triggered.connect(self._quit)
        menu.addAction(open_act)
        menu.addAction(exit_act)
        self.setContextMenu(menu)

    def _show(self) -> None:
        if self.main_window:
            self.main_window.show()
            self.main_window.activateWindow()

    def _quit(self) -> None:
        QApplication.quit()
