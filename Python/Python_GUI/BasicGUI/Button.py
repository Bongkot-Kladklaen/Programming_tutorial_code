from tkinter import *

def B_hello():
    print("Jacop")

root = Tk()
root.geometry("300x300")
b = Button(text="Hello").pack()
b = Button(text="click",command=B_hello).pack()

root.mainloop()