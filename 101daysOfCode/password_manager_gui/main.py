from tkinter import *
from tkinter import messagebox
import random

PAD = 2


# Command functions

def do_generate():
    n_letters = random.randint(4, 8)
    n_numbers = random.randint(2, 4)
    n_symbols = random.randint(2, 4)

    settings = [[n_letters, "letters"], [n_numbers, "numbers"], [n_symbols, "symbols"]]

    for j in range(0, 3):
        for i, setting in enumerate(settings):
            if setting[0] == 0:
                settings.pop(i)

    total_chars = n_letters + n_numbers + n_symbols
    password = ""
    for i in range(0, total_chars):
        if settings:
            rand_index = random.randint(0, len(settings) - 1)
            character = settings[rand_index][1]
            if character == "letters":
                if random.randint(0, 1) == 0:
                    password += chr(random.randint(65, 90))
                else:
                    password += chr(random.randint(97, 122))
            elif character == "numbers":
                password += chr(random.randint(48, 57))
            else:
                password += chr(random.randint(33, 47))
            if settings[rand_index][0] == 1:
                settings.pop(rand_index)
            else:
                settings[rand_index][0] -= 1
    in_pwd.delete(0, END)
    in_pwd.insert(0, password)
    in_pwd.clipboard_append(password)


def do_add():
    if in_web.get() != "" and in_usr.get() != "" and in_pwd.get() != "":
        data_list = [in_web.get(), in_usr.get(), in_pwd.get()]
        string_to_save = "|||".join(data_list) + "\n"
        is_ok = messagebox.askokcancel(title=in_web.get(),
                                       message=f"These are the details entered:\n{string_to_save}\n"
                                               f"Do you want to continue?")
        if is_ok:
            with open("data.txt", "a") as data:
                data.write(string_to_save)
            messagebox.showinfo(title="Success",
                                message=f"Password for {in_web.get()} was saved with success!")
            in_web.delete(0, END)
            in_pwd.delete(0, END)
    else:
        messagebox.showerror(title="Fill all the inputs please!",
                             message="Fill all inputs please!")


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
in_web.focus()

in_usr = Entry(width=35)
in_usr.grid(row=2, column=1, padx=PAD, pady=PAD, columnspan=2)
in_usr.insert(0, 'ondrej17@gmail.com')

in_pwd = Entry(width=25)
in_pwd.grid(row=3, column=1, padx=PAD, pady=PAD)

# Buttons
cmd_generate = Button(text="Generate", command=do_generate)
cmd_generate.grid(row=3, column=2, padx=PAD, pady=PAD)

cmd_add = Button(text="Add entry", command=do_add, width=30)
cmd_add.grid(row=4, column=1, padx=PAD, pady=PAD, columnspan=2)

window.mainloop()
