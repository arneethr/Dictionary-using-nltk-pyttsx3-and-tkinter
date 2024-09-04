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

def meaning():
    query = str(text.get())
    synsets = wordnet.synset('query')
    res = ''
    
    if synsets:
        for syn in synsets:
            res += f'{syn.definition()}\n'
            spokenText.set(res)
            speak("The meaning is "+res)
    else:
        res = 'No definitions found.'
        spokenText.set(res)
        speak(res)
    