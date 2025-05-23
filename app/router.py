# app/router.py

import re
from app import system_module
from app import websearch_module
from app import llm_module

class Router:
    def __init__(self, modules):
        self.modules = modules

    def handle_request(self, text):
        text_lower = text.lower()
        if re.search(r"\b(найди|погода|сайт)\b", text_lower):
            return self.modules['search'].perform_search(text)
        elif re.search(r"\b(открой|удали|создай)\b", text_lower):
            return self.modules['system'].execute_command(text)
        else:
            return self.modules['llm'].query_llm(text)
