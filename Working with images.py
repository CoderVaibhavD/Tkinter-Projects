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
from sys import *
from PIL import ImageTk,Image

root = Tk()
root.title("Hello desginer")
root.iconbitmap('C:\Vaibhav\Calc.ico')

my_img = ImageTk.PhotoImage(Image.open("S:\Images\pendrive.jpg"))
my_label = Label(image=my_img)
my_label.pack()

button_quit = Button(root, text="Exit program", command=root.quit)
button_quit.pack()






root.mainloop()
