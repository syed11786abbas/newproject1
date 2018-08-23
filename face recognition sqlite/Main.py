from Tkinter import *
import cv2
import sqlite3
import numpy as np
from PIL import Image
import os
import tkMessageBox


window = Tk()


    
 
window.title("CHEHRA: The Face Recognition App")
window.configure(background='lightblue')
window.geometry('350x500')




   

def callback1():
    tkMessageBox.showinfo("Help", "Press Q to exit")
    execfile("Intro.py")
    
def callback2():
    execfile("datasetCreator.py")
def callback3():
    execfile("trainer.py")
def callback4():
    execfile("detector.py")
def callback5():
    tkMessageBox.showinfo("Help", "1. Register your face first \n 2. Train your image \n 3.Recognise It")
def callback6():
    window.destroy()
    
lbl = Label(window, text="CHEHRA : THE FACE RECOGNITION APP", width=50, height = 5)
btn1 = Button(window, text="Face Detection", command = callback1, width =30, height = 3)
btn2 = Button(window, text="Face Register",command =callback2,width =30, height = 3)
btn3 = Button(window, text="Training",command =callback3,width =30, height = 3)
btn4 = Button(window, text="Face Recognition",command =callback4,width =30, height = 3)
btn5 = Button(window, text="INSTRUCTIONS",command =callback5, fg ="red",width =30, height = 3)
btn6 = Button(window, text="EXIT",command =callback6, fg ="red",width =30, height = 3)


lbl.grid(row=0,column=1)
btn1.grid(row=1,column=1)
btn2.grid(row=2,column=1)
btn3.grid(row=3,column=1)
btn4.grid(row=4,column=1)
btn5.grid(row=5,column=1)
btn6.grid(row=6,column=1)


 
window.mainloop()
