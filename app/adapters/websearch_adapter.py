# app/adapters/websearch_adapter.py
import requests
from typing import Tuple
from app.core.config import Config

class WebSearchAdapter:
    """Гугл-поиск: читает API_KEY и SEARCH_ENGINE_ID из config.ini."""

    def __init__(self, config_path: str = 'config.ini') -> None:
        cfg = Config(config_path)
        self.api_key = cfg.get('GOOGLE', 'API_KEY')
        self.engine_id = cfg.get('GOOGLE', 'SEARCH_ENGINE_ID')
        if not self.api_key or not self.engine_id:
            raise ValueError("В config.ini отсутствуют GOOGLE:API_KEY или SEARCH_ENGINE_ID")

    def perform_search(self, query: str, num_results: int = 5) -> str:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'key': self.api_key,
            'cx': self.engine_id,
            'q': query,
            'num': num_results,
            'hl': 'ru'
        }
        try:
            resp = requests.get(url, params=params, timeout=10)
            resp.raise_for_status()
        except requests.RequestException as e:
            return f"Ошибка поиска: {e}"
        items = resp.json().get('items', [])
        if not items:
            return "Ничего не найдено."
        first = items[0]
        return f"{first['title']}: {first['snippet']} ({first['link']})"