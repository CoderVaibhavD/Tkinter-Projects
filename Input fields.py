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

e = Entry(root, width=20, bg="Yellow", fg="Black", borderwidth=10)
e.pack()
e.insert(1, "Enter your name: ")

def myClick():
    #You can add an variable - hello = "Hey " + e.get() - and and insert that after text=
    myLabel = Label(root, text="Hey " + e.get())
    myLabel.pack()


myButton = Button(root, text ="Click here!", command = myClick) #can also use hex colour codes (#fff)
myButton.pack()


root.mainloop()



