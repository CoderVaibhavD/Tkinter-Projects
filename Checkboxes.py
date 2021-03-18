#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vaibhav account
#
# Created:     28/07/2020
# Copyright:   (c) vaibhav account 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
from PIL import ImageTk,Image

root=Tk()
root.title("haii")

def show():
    myLabel = Label(root, text=var.get()).pack()

var = StringVar()

c = Checkbutton(root, text="£hety", variable = var, onvalue="Hello", offvalue="bye")
c.deselect()
c.pack()




btn=Button(root, text="Show selection", command=show).pack()



root.mainloop()

