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

root = Tk()
root.title("adding frames")

frame=LabelFrame(root, padx=50, pady=50)
frame.pack(padx=10, pady=10)

b = Button(frame, text="Donmtklshd")
b2 = Button(frame, text="hi")
b.grid(row=0, column=0)
b2.grid(row=1, column=1)




root.mainloop()

