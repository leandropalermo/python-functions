import random
import tkinter as t

import pandas
from pandas import DataFrame
from pandas.errors import EmptyDataError

BACKGROUND_COLOR = "#B1DDC6"

data_list = []
current_card = {}


def start_program():
    try:
        words_to_learn_data = pandas.read_csv("data/words_to_learn.csv")
    except (FileNotFoundError, EmptyDataError):
        words_to_learn_data: DataFrame = pandas.read_csv("data/french_words.csv")
        words_to_learn_data.to_csv("data/words_to_learn.csv", index=False)
    finally:
        global data_list
        data_list = words_to_learn_data.to_dict(orient='records')
        next_card()


def update_list():
    global data_list, current_card
    data_list.remove(current_card)
    words_to_learn_data_updated = pandas.DataFrame.from_records(data_list)
    words_to_learn_data_updated.to_csv("data/words_to_learn.csv", index=False)


def flip_card():
    global current_card
    english_word = current_card.get('English').title()
    canvas.itemconfig(canvas_image, image=back_card)
    canvas.itemconfig(word_text, text=f"{english_word}")
    canvas.itemconfig(title_text, text='English')


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    if data_list:
        current_card = random.choice(data_list)
        french_word = current_card.get('French').title()
        canvas.itemconfig(canvas_image, image=front_card)
        canvas.itemconfig(word_text, text=f"{french_word}")
        canvas.itemconfig(title_text, text='French')
        flip_timer = window.after(3000, func=flip_card)
    else:
        start_program()


def unknown_answer():
    next_card()


def know_answer():
    update_list()
    next_card()


window = t.Tk()
window.title("Flash")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
flip_timer = window.after(3000, func=flip_card)

canvas = t.Canvas(width=800, height=526)
front_card = t.PhotoImage(file="images/card_front.png")
back_card = t.PhotoImage(file="images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=front_card)
canvas.grid(column=0, row=0, columnspan=2)
title_text = canvas.create_text(400, 150, text="French", font=("Ariel", 44, "italic"))
word_text = canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)

unknown_pgn = t.PhotoImage(file="images/wrong.png")
unknown_label = t.Label(image=unknown_pgn)
unknown_button = t.Button(image=unknown_pgn, command=unknown_answer, borderwidth=0, bg=BACKGROUND_COLOR,
                          highlightthickness=0)
unknown_button.grid(column=0, row=1)

know_pgn = t.PhotoImage(file="images/right.png")
know_label = t.Label(image=know_pgn)
know_button = t.Button(image=know_pgn, command=know_answer, borderwidth=0, bg=BACKGROUND_COLOR, highlightthickness=0)
know_button.grid(column=1, row=1)

start_program()
t.mainloop()
