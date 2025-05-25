# app/core/system_service.py
import psutil
import os
from app.core.config import Config

class SystemService:
    """Системные команды: CPU, RAM, создание папок (DEFAULT_FOLDER из config.ini)."""

    def __init__(self, config_path: str = 'config.ini') -> None:
        cfg = Config(config_path)
        self.default_folder = cfg.get('SYSTEM', 'DEFAULT_FOLDER', fallback='NewFolder')

    def execute_command(self, text: str) -> str:
        lower = text.lower()
        if "процессора" in lower:
            return f"CPU загружен на {psutil.cpu_percent()}%"
        elif "свободной памяти" in lower:
            return f"ОЗУ занято на {psutil.virtual_memory().percent}%"
        elif "создай папку" in lower:
            os.makedirs(self.default_folder, exist_ok=True)
            return f"Папка '{self.default_folder}' создана."
        else:
            return "Не распознал команду."