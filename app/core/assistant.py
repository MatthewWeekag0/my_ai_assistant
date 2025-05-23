# core/assistant.py
class Assistant:
    def __init__(self, dialog_manager, llm_client):
        self.dialog_manager = dialog_manager
        self.llm_client = llm_client

    def process_input(self, user_input):
        context = self.dialog_manager.get_context()
        response = self.llm_client.get_response(user_input, context)
        self.dialog_manager.update_history(user_input, response)
        return response
