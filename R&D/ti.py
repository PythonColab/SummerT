from tkinter import *
from tkinter import messagebox
top = Tk()
back = Frame(master=top, width=500, height=500, bg='black')

C = Canvas(top, bg="blue")
filename = PhotoImage(file = "E:\\bhanu1.png")
background_label = Label(top, image=filename)
background_label.place(x=0, y=0, relwidth=1, relheight=1)
C.pack()
lbl = Label(top, text="Hello",bg='red')
lbl.pack()
top.mainloop()
