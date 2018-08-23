from Tkinter import *
import cv2
import sqlite3
import numpy as np
from PIL import Image
import os
import tkMessageBox



window = Tk()
window.title("CHEHRA:The Face Recognition App")
window.configure(background='lightblue')
window.geometry('350x300')

def log():
    
    if (e1.get()=='cse')and(e2.get()=='integral'):
        execfile("Main.py")
        window.destroy()
    
    else:
        tkMessageBox.showinfo("Warning", "Wrong Password")


Label(window, text="User Name", bg='lightblue',fg='red').grid(row=1,column=1)
Label(window, text="Password",bg='lightblue',fg='red').grid(row=3,column=1)

e1 = Entry(window,textvariable=StringVar())
e2 = Entry(window,show='*',textvariable=StringVar())


e1.grid(row=2, column=1)
e2.grid(row=4, column=1)
btn1 = Button(window, text="LOG IN", command = log)
lbl = Label(window, text="CHEHRA: LOGIN PAGE", bg='lightblue',width=50, height = 4)



btn1.grid(row=5, column=1)
lbl.grid(row=0,column=1)

window.mainloop()
