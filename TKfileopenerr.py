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
from tkinter import filedialog

root = Tk()
root.title("adding frames")

root.filename = filedialog.askopenfilename(initialdir="C:\Vaibhav\Images", title="stuff", filetypes=(("png files", "* .png"), ("jpeg files", "*.jpeg")))


def open():#
    global myimg
    root.filename = filedialog.askopenfilename(initialdir="C:\Vaibhav\Images", title="stuff", filetypes=(("png files", "* .png"), ("jpeg files", "*.jpeg")))
    Button(root, text="Click to open folder", command=root.filename).pack()
    my_label = Label(root, text=root.filename).pack()
    myimg=ImageTk.PhotoImage(Image.open(root.filename))
    myimglabel=Label(root, image=myimg).pack()

mybtn=Button(root, text="open file", command=open).pack()


root.mainloop()

