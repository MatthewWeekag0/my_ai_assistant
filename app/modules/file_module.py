# app/file_module.py
import os
import shutil
from typing import List

class FileModule:
    """
    Операции с файловой системой: list, copy и т.п.
    """

    def list_dir(self, path: str) -> List[str]:
        try:
            return os.listdir(path)
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
