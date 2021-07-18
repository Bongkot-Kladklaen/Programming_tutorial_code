from tkinter import *

d = {'thai':'th','japanese':'jp','korean':'kr','chinese':'cn'}
def on_select(e):
    print(e.widget['text'], e.widget['value'])

root = Tk()
root.option_add('*Font','consolas 20')
tv_code = StringVar()
tv_code.set('thai')
n_col = 3
i=0
for k,v in d.items():
    r = Radiobutton(root,text=k, value=v ,variable=tv_code,indicatoron=False, width=11)
    r.bind("<Button-1>",on_select)
    r.grid(row= i // n_col,column=i % n_col)
    i+=1

root.mainloop()