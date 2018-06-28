"""
from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
def clicked():
    lbl.configure(text="Button was clicked !!")
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=1, row=0)
def clicked1():
    lbl.configure(text="Bhanu")
btn1 = Button(window, text="Click Me", command=clicked1)
btn1.grid(column=0, row=1)
window.mainloop()
"""
from tkinter import *
window = Tk()
window.title("Welcome to LikeGeeks app")
window.geometry('350x200')
lbl = Label(window, text="Hello")
lbl.grid(column=0, row=0)
lbl1.pack()
txt = Entry(window,width=10)
txt.grid(column=1, row=0)
def clicked():
    res = "Welcome to " + txt.get()
    lbl.configure(text= res)
btn = Button(window, text="Click Me", command=clicked)
btn.grid(column=2, row=0)
window.mainloop()
