# app/adapters/voice_adapter.py
import speech_recognition as sr
import pyttsx3
from typing import Any
from app.core.config import Config

class VoiceAdapter:
    """Голосовой адаптер: читает LANGUAGE и TTS_ENGINE из config.ini."""

    def __init__(self, router: Any, config_path: str = 'config.ini') -> None:
        cfg = Config(config_path)
        language = cfg.get('VOICE', 'LANGUAGE', fallback='ru-RU')
        engine_name = cfg.get('VOICE', 'TTS_ENGINE', fallback='sapi5')

        self.router = router
        try:
            self.engine = pyttsx3.init(driverName=engine_name)
        except Exception as e:
            raise RuntimeError(f"Не удалось инициализировать TTS-движок '{engine_name}': {e}")
        self.language = language

    def listen(self, timeout: int = 5) -> str:
        recognizer = sr.Recognizer()
        with sr.Microphone() as src:
            try:
                audio = recognizer.listen(src, timeout=timeout)
            except sr.WaitTimeoutError:
                return "Превышено время ожидания микрофона."
        try:
            return recognizer.recognize_google(audio, language=self.language)
        except sr.UnknownValueError:
            return "Не удалось распознать речь."

    def speak(self, text: str) -> None:
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_and_reply(self) -> str:
        text = self.listen()
        if not text:
            return text
        response = self.router.handle_request(text)
        self.speak(response)
        return response