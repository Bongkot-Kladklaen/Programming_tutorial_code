from tkinter import *
from tkinter import messagebox
mp = Tk()
mp.geometry("200x140")
mp.title('First Program')
def confirm():
    messagebox.showinfo('Info', 'To be confirmed.')
    
lb = Label(mp, text = 'Order Confirmation')
lb.pack()
bt = Button(mp, text = 'Accept', bg = 'blue', fg = 'white', command = confirm)
bt.place(x = 75,y = 60)
mp.mainloop()
