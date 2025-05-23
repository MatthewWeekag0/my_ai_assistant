# app/file_module.py

import os
import shutil

class FileModule:
    def list_dir(self, path):
        try:
            return os.listdir(path)
        except FileNotFoundError:
            return f"Путь '{path}' не найден."

    def copy(self, src, dst):
        try:
            shutil.copy(src, dst)
            return f"Файл {src} скопирован в {dst}."
        except FileNotFoundError:
            return f"Файл '{src}' не найден."
