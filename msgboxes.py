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

root = Tk()
root.title("adding frames")

# showinfo, showwaring, showerror,askquestion , askokcancel, askyesno

def popup ():
    res = messagebox.showinfo("This hw", "Hello")
    Label(root, text="You clicked...").pack()
    print(res)

    #if res == 1:
        #Label(root, text="yes").pack()

    #else:
        #Label(root, text="no").pack()


Button(root, text="popup", command=popup).pack()



root.mainloop()

