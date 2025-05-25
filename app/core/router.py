# app/router.py
import re
from typing import Any, Dict

class Router:
    """
    Перенаправляет запросы к нужным модулям по ключевым словам.
    """

    def __init__(self, modules: Dict[str, Any]) -> None:
        self.modules = modules

    def handle_request(self, text: str) -> str:
        text_lower = text.lower()
        if re.search(r"\b(найди|погода|сайт)\b", text_lower):
            return self.modules['search'].perform_search(text)
        elif re.search(r"\b(открой|удали|создай)\b", text_lower):
            return self.modules['system'].execute_command(text)
        else:
            return self.modules['clients'].query_llm(text)
