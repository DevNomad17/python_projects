from tkinter import *


MILE2KM = 1.60934


def do_calculate():
    global state
    if state == 'mile2km':
        res = f"{(float(in_num.get()) * MILE2KM):.2f}"
    else:
        res = f"{(float(in_num.get()) / MILE2KM):.2f}"

    lbl_result.config(text=res)


def do_invert():
    global state
    if state == 'mile2km':
        state = 'km2mile'
        lbl_unit1.config(text="Km")
        lbl_unit2.config(text="Mile")
    else:
        state = 'mile2km'
        lbl_unit1.config(text="Mile")
        lbl_unit2.config(text="Km")
    in_num.delete(0, END)
    in_num.insert(END, string=lbl_result.cget("text"))
    do_calculate()


# Creating a new window and configurations
window = Tk()
window.title("Mile / Km Converter")
window.minsize(width=300, height=100)

state = 'mile2km'

in_num = Entry(width=15)
in_num.grid(row=0, column=1, padx=10, pady=10)

lbl_unit1 = Label(text="Miles")
lbl_unit1.grid(row=0, column=2, padx=10, pady=10)

lbl_is_equal_to = Label(text="is equal to")
lbl_is_equal_to.grid(row=1, column=0, padx=10, pady=10)

lbl_result = Label(text="")
lbl_result.grid(row=1, column=1, padx=10, pady=10)

lbl_unit2 = Label(text="Km")
lbl_unit2.grid(row=1, column=2, padx=10, pady=10)

cmd_calculate = Button(text="Calculate", command=do_calculate)
cmd_calculate.grid(row=2, column=1, padx=10, pady=10)

cmd_invert = Button(text="Invert", command=do_invert)
cmd_invert.grid(row=2, column=2, padx=10, pady=10)



window.mainloop()
