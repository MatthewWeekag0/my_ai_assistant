# app/adapters/websearch_adapter.py
import requests
import configparser
import os
from typing import Tuple, Any

class WebSearchModule:
    """
    Поиск через Google Custom Search API.
    """

    def __init__(self, config_path: str = 'config.ini') -> None:
        self.api_key, self.search_engine_id = self._load_config(config_path)

    def _load_config(self, config_path: str) -> Tuple[str, str]:
        if not os.path.isfile(config_path):
            raise FileNotFoundError(f"Конфиг '{config_path}' не найден.")
        cfg = configparser.ConfigParser()
        cfg.read(config_path)
        try:
            return cfg['GOOGLE']['API_KEY'], cfg['GOOGLE']['SEARCH_ENGINE_ID']
        except KeyError as e:
            raise KeyError(f"В секции [GOOGLE] отсутствует ключ: {e}")

    def perform_search(self, query: str, num_results: int = 5) -> str:
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'key': self.api_key,
            'cx': self.search_engine_id,
            'q': query,
            'num': num_results,
            'hl': 'ru'
        }
        try:
            resp = requests.get(url, params=params)
            resp.raise_for_status()
            items = resp.json().get('items', [])
            if not items:
                return "Ничего не найдено."
            first = items[0]
            return f"{first['title']}\n{first['snippet']}\n{first['link']}"
        except requests.RequestException as e:
            return f"Ошибка поиска: {e}"
