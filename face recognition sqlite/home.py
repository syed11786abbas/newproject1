from Tkinter import *
import cv2
import sqlite3
import numpy as np
from PIL import Image
import os
import tkMessageBox


root = Tk();
root.title("CHEHRA:The Face Recognition App")
root.configure(background='lightblue')
root.geometry("540x500")

def line():
    execfile("login.py")
def ins():
    tkMessageBox.showinfo("Instructions", "1. Press 'CONTINUE' to LOG IN \n 2.After login, register your face \n 3.Train it for further process \n 4. Process it for recognition")


    

b = Button(root, text="CONTINUE", command = line,height=3,width=20,fg="blue")

lb1 = Label(root, text="VIDEO BASED FACE REOGNITION ON REAL-TIME DATA",height=4,fg='blue',bg='lightblue')


lb2 = Label(root, text="This real time face recognition system is capable of identifying or verifying a person from a video frame.\nTo recognize the face in a frame, first you need to detect whether the face is present in the frame",height=3,fg='red',bg='lightblue')

lb3 = Label(root, text="It is based on two major technologies Python and OpenCV",height=3,fg='red',bg='yellow')
lb4 = Label(root, text="TEAM MEMBER",height=3,fg='red',bg='lightblue')
lb5 = Label(root, text="SHUBHANKAR MISHRA \n SYED GHULAM ABBAS \n SHUBHAM SRIVASTAVA \n VIPUL MATHUR",height=4,fg='red',bg='lightblue')
lb6 = Label(root, text="CHEHRA: THE FACE RECOGNITION APP",height=3,fg='DARKBLUE',bg='lightblue')
lb7 = Label(root, text="Click below to continue",height=2,fg='red',bg='lightblue')
b1 = Button(root, text="INSTRUCTIONS", command = ins,height=3,width=20,fg="blue")


lb1.grid()
lb2.grid()
lb3.grid()
lb4.grid()
lb5.grid()
lb6.grid()
b1.grid()
lb7.grid()
b.grid()

root.mainloop()
 
