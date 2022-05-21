from tkinter import *

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
timer = None
reps = 0


# ---------------------------- TIMER RESET ------------------------------- #

def reset_timer():
    global reps
    if not reps:
        return
    reps = 0
    canvas.itemconfig(timer_text, text="00:00")
    window.after_cancel(timer)
    checkmarks_label.config(text="")
    timer_label.config(text="Timer", fg=GREEN)

# ---------------------------- TIMER MECHANISM ------------------------------- #

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    count_mins = int(count / 60)
    count_secs = count % 60
    canvas.itemconfig(timer_text, text=f"{count_mins}:{count_secs:02d}")

    if count:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        checkmark_string = "✓" * int(reps / 2)
        checkmarks_label.config(text=checkmark_string)
        start_timer()


def start_timer():
    global reps
    reps += 1

    if reps % 2 == 1:
        count_down(WORK_MIN * 60)
        timer_label.config(text="Work", fg=GREEN)
    elif reps % 8 != 0:
        count_down(SHORT_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=PINK)
    else:
        count_down(LONG_BREAK_MIN * 60)
        timer_label.config(text="Break", fg=RED)


def start_button_command():
    if reps:
        return
    start_timer()


def reset_button_command():
    reset_timer()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

timer_label = Label(text="Timer", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 36, "bold"))
timer_label.grid(column=1, row=0)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
tomato_image = PhotoImage(file="tomato.png")
canvas.create_image(100, 111, image=tomato_image)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 26, "bold"))
canvas.grid(column=1, row=1)

start_button = Button(text="Start", command=start_button_command, highlightthickness=0)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", command=reset_button_command, highlightthickness=0)
reset_button.grid(column=2, row=2)

checkmarks_label = Label(text="", bg=YELLOW, fg=GREEN, font=(FONT_NAME, 12, "bold"))
checkmarks_label.grid(column=1, row=3)

# ---------------------------- mainloop ------------------------------- #
window.mainloop()
