# app/voice_module.py

import speech_recognition as sr
import pyttsx3

class VoiceModule:
    def __init__(self, router):
        self.router = router

    def listen_and_reply(self):
        r = sr.Recognizer()
        with sr.Microphone() as src:
            audio = r.listen(src, timeout=5)
        try:
            text = r.recognize_google(audio, language="ru-RU")
        except sr.UnknownValueError:
            return "Не распознал речь."
        reply = self.router.handle_request(text)
        engine = pyttsx3.init()
        engine.say(reply)
        engine.runAndWait()
        return reply
