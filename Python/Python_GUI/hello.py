import tkinter as tk

root = tk.Tk()
root.option_add("*Font", "consolas 20")
root.title("Hello World")
for i in range(10):
    tk.Label(root,text = "hello world" ).grid() # Lable -> widget
root.mainloop()