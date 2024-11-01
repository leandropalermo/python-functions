import math
import tkinter as t

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- #

# ---------------------------- TIMER MECHANISM ------------------------------- # 

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# ---------------------------- UI SETUP ------------------------------- #

def start_time():
    global reps
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    reps += 1

    if reps % 8 == 0:
        timer_label.config(fg=RED, text="Break")
        count_down(long_break_sec)
    elif reps % 2 == 0:
        timer_label.config(fg=PINK, text="Break")
        count_down(short_break_sec)
    else:
        timer_label.config(fg=GREEN, text="Work")
        count_down(work_sec)


def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60

    if len(str(count_sec)) == 1:
        count_sec = f"0{count_sec}"

    if len(str(count_min)) == 1:
        count_min = f"0{count_min}"

    canvas.itemconfig(time_set, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_time()
        mark = ""
        work_session = math.floor(reps / 2)
        for _ in range(work_session):
            mark += "✔"

def reset():
    window.after_cancel(timer)
    timer_label.config(fg=GREEN, text="Timer")
    canvas.itemconfig(time_set, text=f"00:00")
    check_label.config(text="")
    global reps
    reps = 0



window = t.Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = t.Label(text="Timer")
timer_label.grid(column=1, row=0)
timer_label.config(font=(FONT_NAME, 35), fg=GREEN, bg=YELLOW)

canvas = t.Canvas(width=205, height=225, bg=YELLOW, highlightthickness=0)
tomato_png = t.PhotoImage(file="tomato.png")
canvas.create_image(103, 112, image=tomato_png)
time_set = canvas.create_text(103, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start_button = t.Button(text="Start", bg=YELLOW, borderwidth=-1, command=start_time)
start_button.grid(column=0, row=2)

reset_button = t.Button(text="Reset", bg=YELLOW, borderwidth=-1, command=reset)
reset_button.grid(column=2, row=2)

check_label = t.Label()
check_label.grid(column=1, row=3)
check_label.config(fg=GREEN, bg=YELLOW)

window.mainloop()
