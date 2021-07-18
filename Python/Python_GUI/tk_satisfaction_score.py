from tkinter import *

fellings = ['vd','d','n','s','vs']
images = [f'{s}.png' for s in fellings]
scores = {s:0 for s in fellings}

def on_click(e):
    global scores
    selected = e.widget['text']
    # print(selected)
    scores[selected] += 1
    print(scores)


root = Tk()

photos = [PhotoImage(file=img) for img in images]
for i in range(len(images)):
    btn = Label(root,image=photos[i], text=fellings[i], bg="white")
    btn.pack(side=LEFT)
    btn.bind("<Button-1>",on_click)

root.mainloop()