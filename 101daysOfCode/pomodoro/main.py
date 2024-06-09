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

# ---------------------------- TIMER RESET ------------------------------- #
def do_reset():
    pass
# ---------------------------- TIMER MECHANISM ------------------------------- #
def do_start():
    pass
# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=50, pady=50, bg=YELLOW)

lbl_heading = Label(text="Timer", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
lbl_heading.grid(row=0, column=1)

cnv_canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
cnv_canvas.create_image(100, 112, image=tomato_img)
cnv_canvas.create_text(102, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
cnv_canvas.grid(row=1, column=1)

cmd_start = Button(text="Start", command=do_start)
cmd_start.grid(row=2, column=0)

cmd_reset = Button(text="Reset", command=do_reset)
cmd_reset.grid(row=2, column=2)

lbl_check = Label(text="✔", fg=GREEN, font=(FONT_NAME, 35, "bold"), bg=YELLOW)
lbl_check.grid(row=3, column=1)

window.mainloop()
