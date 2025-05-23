# app/word_module.py

import docx
import os

class WordModule:
    def __init__(self, router):
        self.router = router

    def analyze(self, filepath):
        if not os.path.isfile(filepath):
            return f"Файл '{filepath}' не найден."

        try:
            doc = docx.Document(filepath)
        except Exception as e:
            return f"Ошибка при открытии файла: {e}"

        paragraphs = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
        if not paragraphs:
            return "Документ не содержит текста для анализа."

        full_text = "\n".join(paragraphs)
        prompt = f"Проверь следующий текст на орфографические и грамматические ошибки:\n\n{full_text}"
        return self.router.handle_request(prompt)
