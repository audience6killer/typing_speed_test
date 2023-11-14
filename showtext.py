import tkinter as tk
import requests
import json

# Get all words: Do not use
get_all_url = "https://random-word-api.herokuapp.com/all"

# Set Lang
set_language_url = "https://random-word-api.herokuapp.com/word?lang=es"

# Request a number of words
get_n_words_url = "https://random-word-api.herokuapp.com/word"

# Set length of requestd words
set_length_url = "https://random-word-api.herokuapp.com/word?length=5"

# params = {'number': 10}
# request = requests.get(url=get_n_words_url, params=params)
# print(request.json())


class DisplayTextHandler(tk.Label):
    def __init__(self, parent, text, bg, width, font, row, column):
        super().__init__(parent, text=text, bg=bg, width=width, font=font)
        self.grid(row=row, column=column, padx=3, pady=3)

        params = {'number': 50}
        request = requests.get(url=get_n_words_url, params=params)
        print(request.json())
        self.words = request.json()
        self.current_word = 0

    def change_word(self):
        if self.current_word < len(self.words):
            self.current_word += 1
            self.configure(text=self.words[self.current_word])

    def get_word(self):
        return self.words[self.current_word]

    def clear_text(self):
        self.config(text='')

