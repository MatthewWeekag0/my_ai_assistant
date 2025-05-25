# app/ui/__init__.py
from .gui import MainWindow as SimpleGUI
from .mainwindow import MainWindow
from .tray_icon import TrayIcon

__all__ = ["SimpleGUI", "MainWindow", "TrayIcon"]