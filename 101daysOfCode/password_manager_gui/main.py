from tkinter import *

PAD = 2


# Command functions

def do_generate():
    pass

def do_add():
    pass

# Creating a new window and configurations
window = Tk()
window.title("Password Manager")
window.minsize(width=240, height=240)
window.config(padx=20, pady=20)

cnv_canvas = Canvas(width=200, height=200, highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
cnv_canvas.create_image(100, 100, image=logo_img)
cnv_canvas.grid(row=0, column=1)

# Labels
lbl_web = Label(text="Website:")
lbl_web.grid(row=1, column=0, padx=PAD, pady=PAD)

lbl_usr = Label(text="Username / E-mail:")
lbl_usr.grid(row=2, column=0, padx=PAD, pady=PAD)

lbl_pwd = Label(text="Password:")
lbl_pwd.grid(row=3, column=0, padx=PAD, pady=PAD)

# Inputs
in_web = Entry(width=35)
in_web.grid(row=1, column=1, padx=PAD, pady=PAD, columnspan=2)

in_usr = Entry(width=35)
in_usr.grid(row=2, column=1, padx=PAD, pady=PAD, columnspan=2)

in_pwd = Entry(width=25)
in_pwd.grid(row=3, column=1, padx=PAD, pady=PAD)

# Buttons
cmd_generate = Button(text="Generate", command=do_generate)
cmd_generate.grid(row=3, column=2, padx=PAD, pady=PAD)

cmd_add = Button(text="Add entry", command=do_add)
cmd_add.grid(row=4, column=1, padx=PAD, pady=PAD, columnspan=2)

window.mainloop()

