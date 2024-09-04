# Arneeth's Dictionary

## Overview

**Arneeth's Dictionary** is a simple desktop application built using Python and Tkinter. It allows users to input a word and receive its definition through text and spoken output. The application uses the `nltk` library to fetch word definitions from WordNet, a large lexical database for the English language, and the `pyttsx3` library for text-to-speech functionality.

## Features

- **Word Lookup**: Enter a word and get its definition(s) displayed in the application.
- **Text-to-Speech**: The definition of the word is read aloud using the `pyttsx3` text-to-speech engine.
- **User-Friendly Interface**: The application provides a simple and intuitive interface built with Tkinter.

## Installation

### Prerequisites

Before running the application, ensure you have the following installed:

- Python 3.x
- Tkinter (usually included with Python installations)
- `nltk` library
- `pyttsx3` library

### Step-by-Step Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/yourusername/arneeths-dictionary.git
    cd arneeths-dictionary
    ```

2. **Install Required Python Libraries**:
    ```bash
    pip install nltk pyttsx3
    ```

3. **Download WordNet Data**:
    The application uses the WordNet corpus, which needs to be downloaded if not already available. You can run the following command to download the data:
    ```python
    import nltk
    nltk.download('wordnet')
    ```

## Usage

1. **Run the Application**:
    ```bash
    python arneeths_dictionary.py
    ```

2. **How to Use**:
   - Enter a word in the provided text entry box.
   - Click on the "Speak Meaning" button.
   - The definition(s) of the word will be displayed, and the application will read the definition aloud.

## Code Explanation
### 1. **Importing Required Libraries**
```python
import nltk, pyttsx3
from nltk.corpus import wordnet
from tkinter import *
```
- **nltk**: The Natural Language Toolkit, a library used for processing human language data. Here, it's used for accessing WordNet, a lexical database of English words.
- **pyttsx3**: A Python library that converts text to speech (TTS).
- **wordnet**: A module in NLTK that provides access to the WordNet database.
- **tkinter**: A Python standard library for creating graphical user interfaces (GUIs).

### 2. **Downloading WordNet Data**
```python
nltk.download('wordnet')
```
- This command ensures that the WordNet data is downloaded and available for use. WordNet contains a rich set of words and their meanings, synonyms, antonyms, etc.

### 3. **Defining the `speak` Function**
```python
def speak(audio):
    engine = pyttsx3.init('sapi5')
    voices = engine.getProperty('voices')
    engine.setProperty('voice',voices[0].id)
    engine.say(audio)
    engine.runAndWait()
```
- **speak(audio)**: A function that uses `pyttsx3` to convert the provided `audio` string into speech.
  - **pyttsx3.init('sapi5')**: Initializes the TTS engine using SAPI5, a speech API supported on Windows.
  - **voices = engine.getProperty('voices')**: Retrieves a list of available voices.
  - **engine.setProperty('voice', voices[0].id)**: Sets the voice to the first available voice (usually the default male voice).
  - **engine.say(audio)**: Queues the text (`audio`) for speech.
  - **engine.runAndWait()**: Processes the speech queue and ensures that the text is spoken before proceeding.

### 4. **Defining the `find_synonym` Function**
```python
def find_synonym(word):
    syn_word = set()
    for syn in wordnet.synset(word):
        for lemma in syn.lemmas():
            syn_word.add(lemma.name())
    return list(syn_word)
```
- **find_synonym(word)**: This function is intended to find synonyms for the given `word`, but there is an issue here:
  - **wordnet.synset(word)** is incorrect because it should be **wordnet.synsets(word)** (plural). `synsets()` returns a list of synsets (meanings) for a word, whereas `synset()` expects a specific synset ID.
  - The function attempts to collect synonyms by iterating through the lemmas (words related to a synset) and adding them to a set to avoid duplicates.
  - The synonyms are then returned as a list.

### 5. **Defining the `meaning` Function**
```python
def meaning():
    query = str(text.get())
    synsets = wordnet.synsets(query)
    res = ''
    
    if (synsets):
        for syn in synsets:
            res += f'{syn.definition()}\n'
        spokenText.set(res)
        speak("The meaning is "+res)
    else:
        res = 'No definitions found.'
        spokenText.set(res)
        speak(res)
```
- **meaning()**: This function retrieves the meaning of the word entered by the user.
  - **query = str(text.get())**: Fetches the user input from the `Entry` widget.
  - **synsets = wordnet.synsets(query)**: Retrieves a list of synsets (meanings) for the input word.
  - **res**: A string variable to store the definitions.
  - If synsets are found:
    - It iterates over each synset, appending its definition to `res`.
    - The definition is displayed in the GUI and spoken aloud.
  - If no synsets are found:
    - It sets `res` to "No definitions found." and displays/speaks this message.

### 6. **Setting Up the GUI**
```python
win = Tk()
win.title("Arneeth's Dictionary")
win.geometry('700x300')
win.config(bg='SlateGray1')
```
- **win = Tk()**: Initializes the main window of the application.
- **win.title("Arneeth's Dictionary")**: Sets the title of the window.
- **win.geometry('700x300')**: Defines the window size as 700x300 pixels.
- **win.config(bg='SlateGray1')**: Sets the background color of the window to "SlateGray1".

### 7. **Creating GUI Widgets**
```python
text = StringVar(win)
spokenText = StringVar(win)

Label(win, text="Arneeth - Dictionary", bg='SlateGray1', fg='gray30', font=('Times', 20, 'bold')).place(x=100, y=10)
Label(win, text='Please enter the word', bg='SlateGray1', font=('calibre', 13, 'normal'), anchor="e", justify=LEFT).place(x=20, y=70)
Entry(win, textvariable=text, width=35, font=('calibre', 13, 'normal')).place(x=20, y=110)
queryLabel = Label(win, textvariable=spokenText, bg='SlateGray1', anchor="e", font=('calibre', 13, 'normal'), justify=LEFT, wraplength=500).place(x=20, y=130)
spokenText.set("Which word do you want to find the meaning of, sir/madam?")
speak("Which word do you want to find the meaning of, sir or madam")
Button(win, text="Speak Meaning", bg='SlateGray4', font=('calibre', 13), command=meaning).place(x=230, y=250)
```
- **text = StringVar(win)** and **spokenText = StringVar(win)**: `StringVar` is a Tkinter variable class that holds a string. Here, it binds the text entry field and the output label to respective variables.
- **Label()**: Creates a text label widget.
  - The first label displays the title "Arneeth - Dictionary".
  - The second label prompts the user to enter a word.
- **Entry()**: Creates an input field for the user to enter a word.
  - **textvariable=text** binds the entry field to the `text` variable.
- **queryLabel**: Displays the result or output. It is bound to `spokenText` to dynamically show the word's definition.
- **Button()**: Creates a button labeled "Speak Meaning" that triggers the `meaning` function when clicked.

### 8. **Starting the Tkinter Event Loop**
```python
win.mainloop()
```
- **win.mainloop()**: Starts the Tkinter event loop, keeping the window open and responsive to user interactions.

### Summary
- The code creates a simple dictionary application using Tkinter for the GUI and NLTK for retrieving word meanings from WordNet. The `pyttsx3` library is used to convert the text output to speech.
- Users can enter a word, and the application will display and speak its meaning. If the word is not found, it will notify the user accordingly.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request or open an issue for any bugs, improvements, or features you'd like to see.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Acknowledgments

- [NLTK](https://www.nltk.org/) for providing the WordNet interface.
- [pyttsx3](https://pypi.org/project/pyttsx3/) for the text-to-speech functionality.
- [Tkinter](https://docs.python.org/3/library/tkinter.html) for the GUI components.

