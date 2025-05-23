# app/system_module.py

import psutil
import os

class SystemModule:
    def execute_command(self, text):
        text = text.lower()
        if "процессора" in text:
            cpu = psutil.cpu_percent()
            return f"Загрузка CPU: {cpu}%"
        elif "свободной памяти" in text:
            mem = psutil.virtual_memory().percent
            return f"Использование оперативной памяти: {mem}%"
        elif "создай папку" in text:
            os.makedirs("НоваяПапка", exist_ok=True)
            return "Папка 'НоваяПапка' создана."
        else:
            return "Не понял команду."
