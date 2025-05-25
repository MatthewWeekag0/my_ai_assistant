# app/core/assistant.py
from typing import Any, Dict, List

class Assistant:
    """
    Обрабатывает ввод пользователя, взаимодействует с DialogManager и LLM-клиентом.
    """

    def __init__(self, dialog_manager: Any, llm_client: Any) -> None:
        self.dialog_manager = dialog_manager
        self.llm_client = llm_client

    def process_input(self, user_input: str) -> str:
        """
        Получает ввод от пользователя, запрашивает ответ у LLM и обновляет историю диалога.
        """
        context: List[Dict[str, str]] = self.dialog_manager.get_context()
        response: str = self.llm_client.get_response(user_input, context)
        self.dialog_manager.update_history(user_input, response)
        return response
