from tkinter import *

expression = ""

def drawMainWindow():
    root = Tk()
    root.title("Mini-Calculator")
    return root

def drawMenuBar(root):
    menu = Menu(root)
    menu.add_command(label="Quit", command=root.destroy)
    root.config(menu=menu)
    return menu

def drawDisplay(root):
    display = Entry(root, bg="yellow", fg="red")
    display.grid(row=1, column=0, columnspan=5)
    Label(root).grid(row=2, column=0)
    return display

def collectExpression(keypress):
    global expression
    expression += keypress
    print(expression)
    return expression

def insertExpression(display, keypress):
    display.insert(END, keypress)

def clearDisplay(display, mode):
    global expression
    if mode == "DEL":
        expression = expression[0:len(display.get())-1]
        display.delete(len(display.get())-1, END)
        print(expression)
    elif mode == "DELALL":
        expression = ""
        display.delete(0, END)
        print(expression)

def handleEvents(display, keypress):
    if keypress == "C":
        clearDisplay(display, "DELALL")
    elif keypress == "DEL":
        clearDisplay(display, "DEL")
    elif keypress == ".":
        insertExpression(display, keypress)
        collectExpression(keypress)
    elif keypress == "(":
        insertExpression(display, keypress)
        collectExpression(keypress)
    elif keypress == ")":
        insertExpression(display, keypress)
        collectExpression(keypress)
    elif keypress == "+":
        insertExpression(display, keypress)
        collectExpression(keypress)
    elif keypress == "-":
        insertExpression(display, keypress)
        collectExpression(keypress)
    elif keypress == "x":
        insertExpression(display, keypress)
        collectExpression("*")
    elif keypress == "÷":
        insertExpression(display, keypress)
        collectExpression("/")
    elif keypress == "=":
        global expression
        try:
            result = eval(expression)
            print(result)
            clearDisplay(display, "DELALL")
            insertExpression(display, str(result))
        except:
            clearDisplay(display, "DELALL")
            insertExpression(display, "Error: Can't execute")
    else:
        insertExpression(display, keypress)
        collectExpression(keypress)

def drawCalButton(root, display):
    Button(root, text="1", width=5, fg="blue", command=lambda: handleEvents(display, "1")).grid(row=4, column=0)
    Button(root, text="2", width=5, fg="blue", command=lambda: handleEvents(display, "2")).grid(row=4, column=1)
    Button(root, text="3", width=5, fg="blue", command=lambda: handleEvents(display, "3")).grid(row=4, column=2)
    Button(root, text="4", width=5, fg="blue", command=lambda: handleEvents(display, "4")).grid(row=5, column=0)
    Button(root, text="5", width=5, fg="blue", command=lambda: handleEvents(display, "5")).grid(row=5, column=1)
    Button(root, text="6", width=5, fg="blue", command=lambda: handleEvents(display, "6")).grid(row=5, column=2)
    Button(root, text="7", width=5, fg="blue", command=lambda: handleEvents(display, "7")).grid(row=6, column=0)
    Button(root, text="8", width=5, fg="blue", command=lambda: handleEvents(display, "8")).grid(row=6, column=1)
    Button(root, text="9", width=5, fg="blue", command=lambda: handleEvents(display, "9")).grid(row=6, column=2)
    Button(root, text="0", width=5, fg="blue", command=lambda: handleEvents(display, "0")).grid(row=7, column=1)

    Button(root, text=".", width=5, command=lambda: handleEvents(display, ".")).grid(row=7, column=0)
    Button(root, text="=", width=12, command=lambda: handleEvents(display, "=")).grid(row=8, column=2, columnspan=2)
    Button(root, text="(", width=5, command=lambda: handleEvents(display, "(")).grid(row=8, column=0)
    Button(root, text=")", width=5, command=lambda: handleEvents(display, ")")).grid(row=8, column=1)
    Button(root, text="x", width=5, command=lambda: handleEvents(display, "x")).grid(row=4, column=3)
    Button(root, text="÷", width=5, command=lambda: handleEvents(display, "÷")).grid(row=5, column=3)
    Button(root, text="-", width=5, command=lambda: handleEvents(display, "-")).grid(row=6, column=3)
    Button(root, text="+", width=5, command=lambda: handleEvents(display, "+")).grid(row=7, column=3)
    Button(root, text="C", width=5, command=lambda: handleEvents(display, "C")).grid(row=3, column=3)
    Button(root, text="Del.", width=5, command=lambda: handleEvents(display, "DEL")).grid(row=3, column=2)

def calculator():
    root = drawMainWindow()

    menu = drawMenuBar(root)
    display = drawDisplay(root)

    drawCalButton(root, display)

    mainloop()

if __name__ == "__main__":
    calculator()
