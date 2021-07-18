from tkinter import *

r = Tk()
r.geometry("400x400")

#สร้าง tap menu
menubar = Menu(r)
#สร้าง menu ย่อยลงไปใน tap 
fileMenu = Menu(menubar,tearoff=0)
fileMenu.add_command(label="New")
fileMenu.add_command(label="Open")
fileMenu.add_command(label="Save as")
fileMenu.add_command(label="Close")
menubar.add_cascade(label="File",menu=fileMenu)

#สร้าง menu ย่อยลงไปใน tap 
helpMenu = Menu(menubar,tearoff=0)
helpMenu.add_command(label="a")
helpMenu.add_command(label="b")
menubar.add_cascade(label="Help",menu=fileMenu)

r.config(menu=menubar)

r.mainloop()