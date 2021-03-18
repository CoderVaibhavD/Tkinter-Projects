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
root.geometry("400x400")

vertical = Scale(root, from_=0, to=200)
vertical.pack()

def slide():
    mylabel=Label(root, text= horizontal.get()).pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))

horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)
horizontal.pack()

mylabel=Label(root, text= horizontal.get()).pack()



mybtn=Button(root, text="click me", command=slide).pack()

root.mainloop()

