import random
from tkinter import *
from tkinter import ttk
from tkinter import font


def generator(length):
    low = "abcdefghijklmnopqrstuvwxyz"
    upp = "ABCDEFGHIJKLMNOPQRSTUVXXYZ"
    numb = "0123456789"
    symb = "@#!?-*."
    all = low + upp + numb + symb

    length = 16

    password = "".join(random.sample(all, length))

    res.delete(1, END)
    res.insert(END, password)


root = Tk()

root.title("Password Generator")

lfont = font.Font(root, family="Courier", size=12, weight="bold")

lbl = ttk.Label(
    root, background="#ff4d4d", font=lfont, justify="center",
    text="\nWelcome to Password Generator\nv.0.1\n*****\n"
)
res = ttk.Entry(root, width=32, justify="center", font="Courier 12")
res.insert(END, "Password: ")
btn = ttk.Button(root, text="Generate password")

lbl.grid(row=0, column=0)
res.grid(row=1, column=0)
btn.grid(row=2, column=0)

btn.bind("<Button-1>", generator)

root.mainloop()
