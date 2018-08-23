from Tkinter import *
master = Tk()
def callback():
    execfile("datasetCreator.py")
b = Button(master, text="Face Input", command=callback)
b.pack()
def callback():
    execfile("detector.py")
c = Button(master, text="Face Recognize", command=callback)
c.pack()

mainloop()
