from tkinter import *

def on_click(e):
    # print(selectedOpt.get())
    # countries[selectedOpt.get()]
    tv_string.set(f'you selected {selectedOpt.get()} ({countries[selectedOpt.get()]})')
root = Tk()
root.option_add('*Font','consolas 25')
# countries = ['Thailand','Japan','Korea']
countries = {'Thailand':'TH','Japan':'Jp','Korea':'Kr'}

tv_string = StringVar()
selectedOpt = StringVar()
selectedOpt.set('Thailand')

om = OptionMenu(root, selectedOpt, *countries)
om.config(width=15)
om.grid(row=0,column=0)
btn = Button(root,text='select')
btn.grid(row =0, column=1)
btn.bind("<Button-1>",on_click)
Label(root,textvariable=tv_string).grid(row=1,columnspan=2)
root.mainloop()