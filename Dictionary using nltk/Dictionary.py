import nltk, pyttsx3
from nltk.corpus import wordnet
from tkinter import *

nltk.download('wordnet')

def speak(audio):
    engine = pyttsx3.init('sapi5')
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
        
win = Tk()
win.title("Arneeth's Dictionary")
win.geometry('700x300')
win.config(bg='Grey')

text=StringVar(win)
spokenText=StringVar(win)

Label(win, text="Arneeth - Dictionay", bg='SlateGray1',fg='gray30', font=('Times', 20, 'bold')).place(x=100, y=10)
Label(win, text='Please enter the word', bg='SlateGray1', font=('calibre', 13, 'normal'),anchor="e", justify=LEFT).place(x=20, y=70)
Entry(win, textvariable=text, width=35, font=('calibre', 13, 'normal')).place(x=20, y=110)
queryLabel = Label(win, textvariable=spokenText, bg='SlateGray1', anchor="e",
                   font=('calibre', 13, 'normal'), justify=LEFT, wraplength=500).place(x=20, y=130)
spokenText.set("Which word do you want to find the meaning of, sir/madam?")
speak("Which word do you want to find the meaning of, sir or madam")
Button(win, text="Speak Meaning", bg='SlateGray4', font=('calibre', 13),command=meaning).place(x=230, y=350)
win.mainloop()
