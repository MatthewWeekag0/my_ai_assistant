# app/core/config.py
import os
import configparser

class Config:
    """
    Утилита для чтения настроек из config.ini.
    """

    def __init__(self, path: str = 'config.ini') -> None:
        if not os.path.isfile(path):
            raise FileNotFoundError(f"Config file '{path}' not found.")
        self._cfg = configparser.ConfigParser()
        self._cfg.read(path)

    def get(self, section: str, option: str, fallback=None):
        try:
            return self._cfg.get(section, option)
        except (KeyError, configparser.NoSectionError, configparser.NoOptionError):
            return fallback