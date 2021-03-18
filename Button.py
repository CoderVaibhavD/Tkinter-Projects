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

def myClick():
    myLabel = Label(root, text="Hello Button!")
    myLabel.pack()

myButton = Button(root, text ="Click me!", padx=50, pady=50, command = myClick, fg="black", bg="orange") #can also use x colour codes (#fff)

myButton.pack()


root.mainloop()






