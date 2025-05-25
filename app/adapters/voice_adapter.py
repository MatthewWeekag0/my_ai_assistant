# app/adapters/voice_adapter.py
import speech_recognition as sr
import pyttsx3
from typing import Any

class VoiceModule:
    """
    Голосовой модуль: слушает микрофон и озвучивает ответ.
    """

    def __init__(self, router: Any) -> None:
        self.router = router
        self.engine = pyttsx3.init()

    def listen(self, timeout: int = 5) -> str:
        r = sr.Recognizer()
        with sr.Microphone() as src:
            audio = r.listen(src, timeout=timeout)
        try:
            return r.recognize_google(audio, language="ru-RU")
        except sr.UnknownValueError:
            return ""

    def speak(self, text: str) -> None:
        self.engine.say(text)
        self.engine.runAndWait()

    def listen_and_reply(self) -> str:
        text = self.listen()
        if not text:
            return "Не распознал речь."
        response = self.router.handle_request(text)
        self.speak(response)
        return response
