# app/modules/browser_module.py
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from app.core.config import Config

class BrowserModule:
    """Headless браузер: читает DRIVER_PATH из config.ini."""

    def __init__(self, config_path: str = 'config.ini') -> None:
        cfg = Config(config_path)
        driver_path = cfg.get('BROWSER', 'DRIVER_PATH')
        if not driver_path:
            raise ValueError("В config.ini не задан BROWSER:DRIVER_PATH")
        self.options = Options(); self.options.add_argument("--headless")
        self.driver_path = driver_path

    def get_title(self, url: str) -> str:
        driver = webdriver.Chrome(executable_path=self.driver_path, options=self.options)
        try:
            driver.get(url)
            return driver.title
        finally:
            driver.quit()