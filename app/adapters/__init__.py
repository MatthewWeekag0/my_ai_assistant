# app/adapters/__init__.py
from .telegram_adapter import TelegramAdapter
from .voice_adapter import VoiceAdapter
from .websearch_adapter import WebSearchAdapter
from .word_adapter import WordAdapter

__all__ = [
    "TelegramAdapter", "VoiceAdapter",
    "WebSearchAdapter", "WordAdapter"
]