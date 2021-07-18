from tkinter import *
from tkinter import messagebox
mp = Tk()
mp.geometry("200x170")
mp.title('First Program')
lb = Label(mp, text = 'Please select your sex')
lb.pack()
v1=v2 = IntVar()
r1 = Radiobutton(mp, text = 'Male', variable = v1, value = 1)
r1.var = v1
r1.pack()
r2 = Radiobutton(mp, text = 'Female', variable = v2, value = 2)
r2.var = v2
r2.pack()
def check():
    if r1.var.get() == 1:
       sex = 'Male'
    else:
        sex = 'Female'
    messagebox.showinfo('Info','Your sex : ' + sex)
bt = Button(mp, text = 'Submit', bg = 'blue', fg = 'white', command = check)
bt.pack()
mp.mainloop()
