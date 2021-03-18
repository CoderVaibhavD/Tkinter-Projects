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

#r = IntVar()
#r.set("2")

MODES = [
    ("Cheese pizza", "Cheese pizza"),
    ("Mushrooms", "mushrooms"),
    ("Pineapple", "Pineapple"),
    ("Chicken wings", "Chicken wings"),
    ("Finished? ", "Your food is ordered and is cooking"),
]

pizza = StringVar()
pizza.set("Cheese pizza")


for text, mode in MODES:
    Radiobutton(root, text=text, variable = pizza, value=mode).pack(anchor=W)


def clicked(value):
    Mylabel = Label(root, text=value)
    Mylabel.pack()


#Radiobutton(root, text="Option 1", variable=r, value=1, command=lambda: clicked(r.get())).pack()
#Radiobutton(root, text="Option 2", variable=r, value=2, command=lambda: clicked(r.get())).pack()

#Mylabel = Label(root, text=pizza.get())
#Mylabel.pack()

Mybutton = Button(root, text="Click me", command=lambda: clicked(pizza.get())).pack()

root.mainloop()

