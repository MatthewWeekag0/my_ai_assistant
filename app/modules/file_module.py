# app/modules/file_module.py
import os
import shutil
from typing import List
from app.core.config import Config

class FileModule:
    """Операции с ФС: дефолтный каталог из config.ini."""

    def __init__(self, config_path: str = 'config.ini') -> None:
        cfg = Config(config_path)
        self.default_dir = cfg.get('FILE', 'DEFAULT_DIRECTORY', fallback=os.getcwd())

    def list_dir(self, path: str = None) -> List[str]:
        target = path or self.default_dir
        try:
            return os.listdir(target)
        except FileNotFoundError:
            return []

    def copy(self, src: str, dst: str) -> str:
        try:
            shutil.copy(src, dst)
            return f"'{src}' → '{dst}'"
        except FileNotFoundError:
            return f"Файл '{src}' не найден."
        except Exception as e:
            return f"Ошибка копирования: {e}"

    def remove(self, path: str) -> str:
        try:
            os.remove(path)
            return f"Удалён: {path}"
        except Exception as e:
            return str(e)

    def move(self, src: str, dst: str) -> str:
        try:
            shutil.move(src, dst)
            return f"Перемещено: {src} → {dst}"
        except Exception as e:
            return str(e)