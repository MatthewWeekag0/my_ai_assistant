# app/browser_module.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from typing import Any

class BrowserModule:
    """
    Запускает headless-браузер и возвращает title страницы.
    """

    def __init__(self) -> None:
        opts = Options()
        opts.add_argument("--headless")
        self.driver = webdriver.Chrome(options=opts)

    def get_title(self, url: str) -> str:
        self.driver.get(url)
        title = self.driver.title
        self.driver.quit()
        return title
