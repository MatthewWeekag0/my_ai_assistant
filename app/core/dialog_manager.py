# app/core/dialog_manager.py
from typing import Any, Dict, List

class DialogManager:
    """
    Управляет историей диалога между пользователем и ассистентом.
    """

    def __init__(self) -> None:
        self.history: List[Dict[str, str]] = []

    def get_context(self) -> List[Dict[str, str]]:
        """
        Возвращает текущую историю диалога.
        """
        return self.history

    def update_history(self, user_input: str, response: str) -> None:
        """
        Добавляет новую пару (запрос–ответ) в историю.
        """
        self.history.append({'user': user_input, 'assistant': response})
