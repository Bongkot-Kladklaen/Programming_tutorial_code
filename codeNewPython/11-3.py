from tkinter import *
from tkinter import messagebox
mp = Tk()
mp.geometry("200x140")
mp.title('First Program')
lb = Label(mp, text = 'Name :')
lb.pack(side = LEFT)
en = Entry(mp, bd = 2)
en.pack(side = RIGHT)
def confirm():
    str = en.get()
    messagebox.showinfo('Info', 'Name : ' + str)
bt = Button(mp, text = 'SUBMIT', bg = 'blue', fg = 'white', command = confirm)
bt.place(x = 75,y = 100)
mp.mainloop()
