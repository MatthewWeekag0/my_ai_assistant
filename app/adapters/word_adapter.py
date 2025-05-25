# app/adapters/word_adapter.py
import docx
import os
from typing import List, Any

class WordModule:
    """
    Анализ Word-документа через python-docx.
    """

    def __init__(self, router: Any) -> None:
        self.router = router

    def analyze(self, filepath: str) -> str:
        if not os.path.isfile(filepath):
            return f"Файл '{filepath}' не найден."
        try:
            doc = docx.Document(filepath)
        except Exception as e:
            return f"Ошибка при открытии файла: {e}"

        paragraphs: List[str] = [p.text.strip() for p in doc.paragraphs if p.text.strip()]
        if not paragraphs:
            return "Документ пуст."
        text = "\n".join(paragraphs)
        prompt = f"Проверь текст на ошибки:\n\n{text}"
        return self.router.handle_request(prompt)
