#importing required modules
from tkinter import *
from tkinter import messagebox

#GUI interaction
window = Tk()
window.geometry("570x450")
window.title("Calculator")
window.config(bg = "black")

#Adding widgets and inputs
e = Entry(window, borderwidth = 10, font = ("Comic Sans MS", 30), cursor = "dot")    #Box for Display 
c = Canvas(window, height = 35, bg = "lightgrey")
label = Label(text="-----------------------------------------------------------------------------------------------------------------")

#functions for all tasks
def work(value):
    result = e.get()
    e.delete(0,END)                                                 # Delete from 0 to end of the content to avoid useless repetition
    e.insert(0, str(result) + str(value))                           # insert string at index 0

def clear():
    e.delete(0,END)

def leave():
    ask = messagebox.askyesno("QUIT?","Do you want to leave?")
    if ask:
        window.destroy()

def plus():
    global operator
    global value1
    value1 = e.get()[:-1]
    operator = "+"

def minus():
    global operator
    global value1
    value1 = e.get()[:-1]
    operator = "-"

def mult():
    global operator
    global value1
    value1 = e.get()[:-1]
    operator = "x"

def div():
    global operator
    global value1
    value1 = e.get()[:-1]
    operator = "/"

def equals():
    if "ERROR!" in e.get():
        e.delete(0,END)
    try:
        index = value1.index(value1[-1],-1)
        value2 = e.get()[index+2:]
        if len(value1+value2) > 25:
            messagebox.showerror("Too Long!","Press Clear to continue again!")
        e.delete(0,END)
        if operator == "+":
            e.insert(0, float(value1) + float(value2))
        elif operator == "-":
            e.insert(0, float(value1) - float(value2))
        elif operator == "x":
            e.insert(0, float(value1) * float(value2))
        elif operator == "/":
            e.insert(0, round(float(value1) / float(value2),3))
        else:
            e.insert(0, "ERROR")
    except:
        e.insert(0,"ERROR!")
        messagebox.showinfo("Inavlidity","Press clear to continue again!")

#Buttons Now : 
b = Button(window, cursor = "circle", text = "1", width = 10, font = ("Comic Sans MS", 15), bg = "lightgrey", activebackground = "black", activeforeground = "white", command = lambda :  work(1))
b.place(x = 10, y = 120) 
b = Button(window, cursor = "circle", text = "2", width = 10, font = ("Comic Sans MS", 15), bg = "lightgrey", activebackground = "black", activeforeground = "white", command = lambda :  work(2))
b.place(x = 150, y = 120)
b = Button(window, cursor = "circle", text = "3", width = 10, font = ("Comic Sans MS", 15), bg = "lightgrey", activebackground = "black", activeforeground = "white", command = lambda :  work(3))
b.place(x = 290, y = 120)
b = Button(window, cursor = "circle", text = "+", width = 10, font = ("Comic Sans MS", 15), bg = "lightgrey", activebackground = "black", activeforeground = "white", command = lambda :  [work("+"),plus()])
b.place(x = 430, y = 120)

b = Button(window, cursor = "circle", text = "4", width = 10, font = ("Comic Sans MS", 15), bg = "lightgrey", activebackground = "black", activeforeground = "white", command = lambda :  work(4))
b.place(x = 10, y = 180)
b = Button(window, cursor = "circle", text = "5", width = 10, font = ("Comic Sans MS", 15), bg = "lightgrey", activebackground = "black", activeforeground = "white", command = lambda :  work(5))
b.place(x = 150, y = 180)
b = Button(window, cursor = "circle", text = "6", width = 10, font = ("Comic Sans MS", 15), bg = "lightgrey", activebackground = "black", activeforeground = "white", command = lambda :  work(6))
b.place(x = 290, y = 180)
b = Button(window, cursor = "circle", text = "-", width = 10, font = ("Comic Sans MS", 15), bg = "lightgrey", activebackground = "black", activeforeground = "white", command = lambda :  [work("-"),minus()])
b.place(x = 430, y = 180)

b = Button(window, cursor = "circle", text = "7", width = 10, font = ("Comic Sans MS", 15), bg = "lightgrey", activebackground = "black", activeforeground = "white", command = lambda :  work(7))
b.place(x = 10, y = 240)
b = Button(window, cursor = "circle", text = "8", width = 10, font = ("Comic Sans MS", 15), bg = "lightgrey", activebackground = "black", activeforeground = "white", command = lambda :  work(8))
b.place(x = 150, y = 240)
b = Button(window, cursor = "circle", text = "9", width = 10, font = ("Comic Sans MS", 15), bg = "lightgrey", activebackground = "black", activeforeground = "white", command = lambda :  work(9))
b.place(x = 290, y = 240)
b = Button(window, cursor = "circle", text = "x", width = 10, font = ("Comic Sans MS", 15), bg = "lightgrey", activebackground = "black", activeforeground = "white", command = lambda :  [work("x"),mult()])
b.place(x = 430, y = 240)

b = Button(window, cursor = "circle", text = "/", width = 10, font = ("Comic Sans MS", 15), bg = "lightgrey", activebackground = "black", activeforeground = "white", command = lambda :  [work("/"), div()])
b.place(x = 10, y = 300)
b = Button(window, cursor = "circle", text = "=", width = 10, font = ("Comic Sans MS", 15), bg = "lightgrey", activebackground = "black", activeforeground = "white", command = equals)
b.place(x = 150, y = 300)
b = Button(window, cursor = "circle", text = "Clear", width = 10, font = ("Comic Sans MS", 15), bg = "lightgrey", activebackground = "black", activeforeground = "white", command = clear)
b.place(x = 290, y = 300)
b = Button(window, cursor = "circle", text = "Exit", width = 10, font = ("Comic Sans MS", 15), bg = "lightgrey", activebackground = "black", activeforeground = "white", command = leave)
b.place(x = 430, y = 300)

#packing widgets
e.place(x = 0, y = 0, relwidth = 1)                                 #relwidth = relative width between 0 and 1 as a fraction of parent width
label.place(x = 0, y = 87)
c.pack(side = BOTTOM, fill = X)

#Main Loop
window.mainloop()