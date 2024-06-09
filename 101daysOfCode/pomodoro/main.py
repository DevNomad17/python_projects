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
SECONDS_IN_MINUTE = 60
reps = 0
main_timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def do_reset():
    global reps
    global main_timer

    lbl_check.configure(text="")
    lbl_heading.configure(text="Timer", fg=GREEN)
    reps = 0
    window.after_cancel(main_timer)
    cnv_canvas.itemconfig(timer_text, text="00:00")


# ---------------------------- TIMER MECHANISM ------------------------------- #
def do_start():
    global reps

    reps += 1
    if reps % 2 == 1:
        count_down(WORK_MIN * SECONDS_IN_MINUTE)
        lbl_heading.configure(text="Work", fg=GREEN)
    elif reps == 8:
        count_down(LONG_BREAK_MIN * SECONDS_IN_MINUTE)
        lbl_heading.configure(text="Rest", fg=RED)
    else:
        count_down(SHORT_BREAK_MIN * SECONDS_IN_MINUTE)
        lbl_heading.configure(text="Rest", fg=PINK)
    marks = ""
    for i in range(int(reps / 2)):
        marks += "✔"
    lbl_check.configure(text=marks)
    if reps == 8:
        reps = 0


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global main_timer
    minutes = int(count / 60)
    if minutes < 10:
        minutes = f"0{minutes}"
    seconds = int(count % 60)
    if seconds < 10:
        seconds = f"0{seconds}"
    timer_digits = f"{minutes}:{seconds}"
    cnv_canvas.itemconfig(timer_text, text=timer_digits)
    if count > 0:
        main_timer = window.after(1000, count_down, count - 1)
    else:
        do_start()


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

lbl_heading = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
lbl_heading.grid(row=0, column=1)

cnv_canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
cnv_canvas.create_image(100, 112, image=tomato_img)
timer_text = cnv_canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
cnv_canvas.grid(row=1, column=1)

cmd_start = Button(text="Start", command=do_start)
cmd_start.grid(row=2, column=0)

cmd_reset = Button(text="Reset", command=do_reset)
cmd_reset.grid(row=2, column=2)

lbl_check = Label(fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
lbl_check.grid(row=3, column=1)

window.mainloop()
