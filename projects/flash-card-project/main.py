import pandas as pd
import time
import random
from tkinter import *


# after 3 seconds card flips to ask if i knew it
# check if right
# x if wrong


class Window:
    BACKGROUND_COLOR = "#B1DDC6"
    NATIVE_FONT_COLOR = "#FFFFFF"
    TARGET_FONT_COLOR = "#000000"
    LANGUAGE_FONT = ("Arial", 24, "italic")
    WORD_FONT = ("Arial", 36, "bold")

    def __init__(self):
        self.window = Tk()
        self.window.title("Flashy")
        self.window.config(padx=20, pady=20, bg=self.BACKGROUND_COLOR)
        self.df = pd.read_csv("data/french_words.csv").sample(frac=1).reset_index(drop=True)
        self.current_word_index = 0
        self.wordlist_len = len(self.df)
        self.card_front_image = PhotoImage(file="images/card_front.png")
        self.card_back_image = PhotoImage(file="images/card_back.png")
        self.card_canvas = Canvas(width=800, height=526, bg=self.BACKGROUND_COLOR, highlightthickness=0)
        self.card_canvas_image = self.card_canvas.create_image(400, 263, image=self.card_back_image)
        self.language = self.card_canvas.create_text(400, 150, text="English", fill=self.NATIVE_FONT_COLOR,
                                                     font=self.LANGUAGE_FONT)
        self.word = self.card_canvas.create_text(400, 263, text="word", fill=self.NATIVE_FONT_COLOR,
                                                 font=self.WORD_FONT)
        self.card_canvas.grid(column=0, row=0, columnspan=3, rowspan=2, padx=20, pady=20)
        self.incorrect_image = PhotoImage(file="images/wrong.png")
        self.incorrect_button = Button(image=self.incorrect_image, borderwidth=0, highlightthickness=0,
                                       command=self.incorrect_button_command, state=DISABLED)
        self.incorrect_button.grid(column=0, row=2)
        self.correct_image = PhotoImage(file="images/right.png")
        self.correct_button = Button(image=self.correct_image, borderwidth=0, highlightthickness=0,
                                     command=self.correct_button_command, state=DISABLED)
        self.correct_button.grid(column=2, row=2)
        self.show_target_word()
        mainloop()

    def incorrect_button_command(self):
        self.current_word_index += 1
        self.show_target_word()

    def correct_button_command(self):
        self.df = self.df.drop(self.current_word_index).reset_index(drop=True)
        self.wordlist_len = len(self.df)
        self.df.to_csv("data/french_words_new.csv", index=False)

        self.show_target_word()

    def show_target_word(self):
        self.incorrect_button.config(state=DISABLED)
        self.correct_button.config(state=DISABLED)
        if self.current_word_index >= self.wordlist_len:
            self.current_word_index = 0
            self.df = self.df.sample(frac=1).reset_index(drop=True)

        self.window.createtimerhandler(3000, self.show_native_word)
        self.card_canvas.itemconfig(self.card_canvas_image, image=self.card_front_image)
        self.card_canvas.itemconfig(self.language, text="French", fill=self.TARGET_FONT_COLOR)
        self.card_canvas.itemconfig(self.word, text=self.df.loc[self.current_word_index, "French"],
                                    fill=self.TARGET_FONT_COLOR)

    def show_native_word(self):
        self.card_canvas.itemconfig(self.card_canvas_image, image=self.card_back_image)
        self.card_canvas.itemconfig(self.language, text="English", fill=self.NATIVE_FONT_COLOR)
        self.card_canvas.itemconfig(self.word, text=self.df.loc[self.current_word_index, "English"],
                                    fill=self.NATIVE_FONT_COLOR)
        self.incorrect_button.config(state=NORMAL)
        self.correct_button.config(state=NORMAL)


Window()
