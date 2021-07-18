from tkinter import *
from tkinter import messagebox

def hello(event):
    #message box
    messagebox.showinfo(title='แสดงข้อความ',message='Hello User')

r = Tk()
r.geometry("400x400")
b1 = Button(text="Hello").pack()
b1.bind("<Button-1>",hello)
# txtBox = Entry().pack()
