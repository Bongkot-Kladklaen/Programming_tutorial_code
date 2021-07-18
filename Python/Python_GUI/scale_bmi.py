from tkinter import *

def on_drag(e):
    bmi = w.get() / (h.get() / 100) ** 2
    tv_bmi.set(f'BMI = {bmi:.2f}')
    colo_zone = ""
    if bmi > 30:
        colo_zone = 'red'
    elif bmi >= 25:
        colo_zone = 'orange'
    elif bmi >=23:
        colo_zone = 'yellow'
    elif bmi >= 18.5:
        colo_zone = 'green'
    else:
        colo_zone = 'red'
    lbl_bmi["bg"] = colo_zone
root = Tk()
root.option_add('*Font','consolas 20')
tv_bmi = StringVar()
Label(root, text="weight(kg)").grid(row=0,column=0,sticky='sw',padx=10)
Label(root, text="height(cm)").grid(row=1,column=0,sticky='sw',padx=10)
w = Scale(root,from_=1, to=100, orient=HORIZONTAL,length=200,width=30)
w.set(50)
w.grid(row=0,column=1)
w.bind("<B1-Motion>",on_drag)
w.bind("<Button-1>",on_drag)
h = Scale(root,from_=1, to=200, orient=HORIZONTAL,length=200,width=30)
h.set(160)
h.grid(row=1,column=1)
h.bind("<B1-Motion>",on_drag)
h.bind("<Button-1>",on_drag)
lbl_bmi = Label(root,textvariable=tv_bmi)
lbl_bmi.grid(row=3,columnspan=2,sticky='news')
root.mainloop()