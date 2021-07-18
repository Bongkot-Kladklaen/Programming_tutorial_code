from tkinter import *

root = Tk()
root.option_add('*Font','consolas 25')
# Label(root, text="apple").pack(anchor=E)
# Label(root, text="apple", fg='red').pack()
# Label(root, text="apple", bg='green').pack(anchor=W)
# Label(root, text="apple", fg='red', bg="green").pack(pady = 10)
# Label(root, text="banana",width=15, bg="yellow").pack()
# Label(root, text="coconut",bg="green").pack(fill=X)
# Label(root, text="strawberry",fg='red', bg="green").pack()
# Label(root, text="green\ntea", bg="green").pack(fill=X)
Label(root, text="Happiness in when what you think, what you say, and wat you do are in harmony", bg="gold").pack(fill=X)
Label(root, text="Happiness in when what you think, what you say, and wat you do are in harmony", bg="orange" ,wraplength=400).pack(fill=X)
Label(root, text="Happiness in when what you think, what you say, and wat you do are in harmony", bg="orange" ,wraplength=400,justify=RIGHT).pack(fill=X)


root.mainloop()