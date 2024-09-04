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
    
def find_synonym(word):
    syn_word = set()
    for syn in wordnet.synset(word):
        for lemma in syn.lemmas():
            syn_word.add(lemma.name())
    return list(syn_word)
