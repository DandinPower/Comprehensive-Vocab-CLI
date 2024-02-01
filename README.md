# Comprehensive-Vocab-CLI

Comprehensive-Vocab-CLI is a command-line tool designed to help you learn and remember new words and their meanings. You can input a word, and the tool will provide you with the meaning of the word, synonyms, antonyms, and usage of the word. It also has the ability to play the pronunciation of the word.

## Features

- Fetches and displays detailed explanations of words including their meanings, synonyms, antonyms, and usage.
- Plays the pronunciation of the word.
- Caches the words and their explanations for quick future references.

## Future Improvements

- Implement a database to store the words and their pronunciations.
- Improve the Text-to-Speech feature by using Google Text-to-Speech API.

## Installation

This project requires Python and pip. Once you have these installed, you can install the project dependencies with:

```sh
pip install -r requirements.txt
```

## Usage
To use the Comprehensive-Vocab-CLI, follow these steps:

```
python main.py
```

You will be asked to choose an action:
1. Enter 1 to explain a word. You will be prompted to enter the word. If the word has been searched before, the cached explanation will be displayed. Otherwise, the tool will fetch the explanation and cache it for future use. After the explanation is displayed, you will be asked if you want to play the word's pronunciation.
2. Enter 2 to exit the program.