# app/system_service.py
import psutil
import os

class SystemModule:
    """
    Выполняет простые системные команды по ключевым словам.
    """

    def execute_command(self, text: str) -> str:
        lower = text.lower()
        if "процессора" in lower:
            return f"CPU загружен на {psutil.cpu_percent()}%"
        elif "свободной памяти" in lower:
            return f"ОЗУ занято на {psutil.virtual_memory().percent}%"
        elif "создай папку" in lower:
            os.makedirs("НоваяПапка", exist_ok=True)
            return "Папка 'НоваяПапка' создана."
        else:
            return "Не распознал команду."
