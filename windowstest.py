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
from tkinter import messagebox
import sys

root = Tk()
root.title("adding frames")

def open():
    top = Toplevel()
    root.title("frames")
    btn2 = Button(top, text="Close win", command=top.destroy).pack()


btn=Button(root, text="Open second win", command=open).pack()
btn2=Button(root, text="Close main", command=root.destroy).pack()


root.mainloop()





root.mainloop()

