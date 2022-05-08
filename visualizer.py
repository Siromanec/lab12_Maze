from tkinter import *
import time
from tkinter import font
root=Tk()

variable=StringVar()

def update_label(a):
    for i in a:
        variable.set(str(i))
        root.update()
        #time.sleep(0.01)
def run(a):
    font.nametofont("TkFixedFont").actual()
    your_label=Label(root, textvariable=variable, font='TkFixedFont')
    your_label.pack()
    start_button=Button(root,text="start",command=update_label(a))
    start_button.pack()
    root.mainloop()