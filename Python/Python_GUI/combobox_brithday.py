from datetime import date
from tkinter import *
from tkinter import ttk

def on_click(e):
    # print(cbo_day.get(), cbo_month.get(), cbo_year.get())
    mm = month_list.index(cbo_month.get())
    bd = date(int(cbo_year.get()),mm+1,int(cbo_day.get()))
    tv_string.set(f'{bd}')
    # print(bd)

month_list = ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec']
root = Tk()
root.option_add('*Font','consolas 20')

cbo_day = ttk.Combobox(root, values=list(range(1,32)),width=3,stat='readonly')
cbo_day.current(0)
cbo_day.pack(side=LEFT)

cbo_month = ttk.Combobox(root, values=month_list,width=4,stat='readonly')
cbo_month.current(0)
cbo_month.pack(side=LEFT)

cbo_year = ttk.Combobox(root, values=list(range(1960,2021)),width=4)
cbo_year.current(0)
cbo_year.pack(side=LEFT)

btn = Button(root,text='submit')
btn.pack(side=LEFT)
btn.bind('<Button-1>',on_click)

tv_string = StringVar()
Label(root,textvariable=tv_string).pack(side=LEFT)
root.mainloop()