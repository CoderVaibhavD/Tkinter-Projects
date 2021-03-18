#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vaibhav account
#
# Created:     27/07/2020
# Copyright:   (c) vaibhav account 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *

root = Tk()

#creating a text
#1 step process:

myLabel1 = Label(root, text = "Hello World!")
myLabel2 = Label(root, text = "My name is Vaibhav Dachavaram!")
myLabel3 = Label(root, text = "                            ")

#Show it on the screen
#2 step process:

myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=5)
myLabel3.grid(row=1, column=1)



root.mainloop()






