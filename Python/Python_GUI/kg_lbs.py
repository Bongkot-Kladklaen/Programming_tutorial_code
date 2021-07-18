from tkinter import *
from tkmacosx import Button

root = Tk()
root.option_add("*Font", "impact 20")

def on_click():
    lbs = tv_kg.get() * 2.2
    tv_lbs.set(f'{lbs:.2f} lbs.')

tv_kg = DoubleVar()
tv_lbs = StringVar()

Entry(root, textvariable=tv_kg, width=7, justify=RIGHT).pack(side=LEFT)
Label(root, text="Kg.").pack(side=LEFT)
Button(root, text="=", command=on_click, background="green").pack(side=LEFT)
Label(root, textvariable=tv_lbs).pack(side=LEFT)

root.mainloop()