import nltk, pyttsx3
from nltk.corpus import wordnet
from tkinter import *

nltk.download('wordnet')

def speak(audio):
    engine = pyttsx3.init(sapi5)
    voices = engine.getProperty('voices')
    voice = engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()