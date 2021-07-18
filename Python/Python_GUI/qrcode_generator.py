from tkinter import *
import qrcode
from PIL import Image,ImageTk

def create_qrcode(text):
    qr = qrcode.QRCode()
    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_color="black",back_color="white")
    return img

def demo():
    def on_click(e):
        input_text = txt.get('0.0','end-1c')
        img = create_qrcode(input_text).resize((250,250))
        imgTk = ImageTk.PhotoImage(img)
        qr.configure(image=imgTk)
        qr.image = imgTk

    root = Tk()
    root.title("QR code")
    root.option_add('*Font','colsolas 20')
    Label(root,text='enter text',bg='gray').grid(row = 0,column=0,sticky='news')
    txt = Text(root,height=4,width=30,fg="green")
    txt.insert(END, 'lily')
    txt.grid(row=1,column=0)
    btn = Button(root,text='create QR code')
    btn.grid(row=2,column=0)
    btn.bind("<Button-1>", on_click)
    qr = Label(root)
    qr.grid(row=0,column=1,rowspan=3)
    root.mainloop()
if __name__ == '__main__':
    # create_qrcode('lily').show()
    demo()