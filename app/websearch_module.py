# app/websearch_module.py

import requests
import configparser
import os

class WebSearchModule:
    def __init__(self, config_path='config.ini'):
        self.api_key, self.search_engine_id = self._load_config(config_path)

    def _load_config(self, config_path):
        config = configparser.ConfigParser()
        if not os.path.isfile(config_path):
            raise FileNotFoundError(f"Файл конфигурации '{config_path}' не найден.")
        config.read(config_path)
        try:
            api_key = config['GOOGLE']['API_KEY']
            search_engine_id = config['GOOGLE']['SEARCH_ENGINE_ID']
            return api_key, search_engine_id
        except KeyError as e:
            raise KeyError(f"Отсутствует необходимый параметр в разделе [GOOGLE]: {e}")

    def perform_search(self, query, num_results=5):
        url = "https://www.googleapis.com/customsearch/v1"
        params = {
            'key': self.api_key,
            'cx': self.search_engine_id,
            'q': query,
            'num': num_results,
            'hl': 'ru'
        }
        try:
            response = requests.get(url, params=params)
            response.raise_for_status()
            results = response.json().get('items', [])
            if not results:
                return "По вашему запросу ничего не найдено."
            first_result = results[0]
            title = first_result.get('title')
            snippet = first_result.get('snippet')
            link = first_result.get('link')
            return f"{title}\n{snippet}\n{link}"
        except requests.exceptions.RequestException as e:
            return f"Ошибка при выполнении запроса: {e}"
