from tkinter import *

def on_drag(e):
    color_hex = f'#{sc[0].get():02X}{sc[1].get():02X}{sc[2].get():02X}'
    tv_color.set(color_hex)
    lbl_color["bg"] = color_hex

root = Tk()
root.option_add('*Font','consolas 20')
tv_color = StringVar()
rgb = ['red','green','blue']
sc = []
for i,c in enumerate(rgb):
    Label(root, text=c,fg=c).grid(row=i,column=0,sticky='sw')
    w = Scale(root, from_ = 0, to = 255, orient=HORIZONTAL,length=200,width=30,fg=c)
    w.grid(row=i, column=1)
    w.bind('<B1-Motion>', on_drag)
    w.bind('<Button-1>', on_drag)
    sc.append(w)
# Label(root, text='red',fg='green').grid(row=1,column=0,sticky='sw')
# # Label(root, text='red',fg='blue').grid(row=2,column=0,sticky='sw')

# r = Scale(root, from_ = 0, to = 255, orient=HORIZONTAL,length=200,width=30,fg='red')
# r.grid(row=0,column=1)
# r.bind('<B1-Motion>',on_drag)
# r.bind('<Button-1>',on_drag)
#
# g = Scale(root, from_ = 0, to = 255, orient=HORIZONTAL,length=200,width=30,fg='green')
# g.grid(row=1,column=1)
# g.bind('<B1-Motion>',on_drag)
# g.bind('<Button-1>',on_drag)
#
# b = Scale(root, from_ = 0, to = 255, orient=HORIZONTAL,length=200,width=30,fg='blue')
# b.grid(row=2,column=1)
# b.bind('<B1-Motion>',on_drag)
# b.bind('<Button-1>',on_drag)

lbl_color = Label(root, textvariable=tv_color)
lbl_color.grid(row=3,columnspan=2,sticky='news')

root.mainloop()