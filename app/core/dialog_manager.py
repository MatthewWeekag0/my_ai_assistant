# core/dialog_manager.py
class DialogManager:
    def __init__(self):
        self.history = []

    def get_context(self):
        return self.history

    def update_history(self, user_input, response):
        self.history.append({'user': user_input, 'assistant': response})
