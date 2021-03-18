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


# Drop down menus

def show():
    myLabel=Label(root, text=clicked.get()).pack()

options = [
    "Hello",
    "Pizza",
    "AR"
]

clicked = StringVar()
clicked.set("Hsdo")
#clicked.set(options[0])

drop = OptionMenu(root, clicked, *options)
drop.pack()

btn=Button(root, text="sow select", command=show).pack()


root.mainloop()

