from tkinter import *
from tkmacosx import Button

root = Tk()
root.option_add('*Font','consolas 20')

# Button(root,text='phone', borderwidth=0).pack()
# Button(root,text='camera', bg="orange").pack(fill=X)
# Button(root,text='computer', fg='blue',padx=30).pack()
# Button(root,text='computer', fg='blue', bd=10).pack()
# Button(root,text='computer\ndisabled', fg='blue', bd=10,state=DISABLED).pack()
# Button(root,text='green\ntea', fg='green', bd=10).pack()

photo = PhotoImage(file="yinyang.png")
Button(root,text="yinyang",image=photo , borderless=1).pack()
Button(root,text="yin yang",image=photo, compound=LEFT, borderless=1).pack()
Button(root,text="yin yang",image=photo, compound=LEFT, padx=20,borderless=1).pack()
Button(root,text="yin yang",image=photo, compound=RIGHT,borderless=1).pack()
Button(root,text="yin yang",image=photo, compound=TOP,borderless=1).pack()
Button(root,text="yin yang",image=photo, compound=BOTTOM,borderless=1).pack()

root.mainloop()