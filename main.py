import speech_recognition as sr
from deep_translator import GoogleTranslator
from gtts import gTTS
import os
import pyttsx3

engine = pyttsx3.init()

voice = engine.getProperty('voices')[1]
engine.setProperty('voice', voice.id)
r = sr.Recognizer()

with sr.Microphone() as source:
    print("Starting")
    audio_data = r.listen(source)
    print("Recognizing...")
    text = r.recognize_google(audio_data)
    print(text)


translated = GoogleTranslator(source='auto', target='french').translate(text)
print(translated)


engine.say(translated)
engine.runAndWait()
