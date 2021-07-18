from tkinter import *

def on_click():
    # for i,chk in enumerate(chks):
    #     if chk.get():
    #         print(interests[i])
    lst = [interests[i] for i,chk in enumerate(chks) if chk.get()]
    # print(lst)
    print(','.join(lst))

interests = ['Music','book','Movie','Photography','Game','Travel']
root = Tk()
root.option_add('*Font','consolas 20')
chks = [BooleanVar() for i in interests]

Label(root,text='Your Interests',bg='gold')
for i,s in enumerate(interests):
    r = Checkbutton(root,text=s ,variable=chks[i])
    r.pack(anchor=W)
Button(root,text='submit',command=on_click).pack(anchor=W)
root.mainloop()