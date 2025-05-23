# app/browser_module.py

from selenium import webdriver
from selenium.webdriver.chrome.options import Options

class BrowserModule:
    def __init__(self):
        options = Options()
        options.add_argument("--headless")
        self.driver = webdriver.Chrome(options=options)

    def get_title(self, url):
        self.driver.get(url)
        title = self.driver.title
        self.driver.quit()
        return title
