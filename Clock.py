#-------------------------------------------------------------------------------
# Name:        Clock
# Purpose:
#
# Author:      vaibhav account
#
# Created:     27/07/2020
# Copyright:   (c) vaibhav account 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
import time


root = Tk()
root.title("Clock")
root.geometry("600x400")

def clock():
    hour = time.strftime("%H")
    minute = time.strftime("%M")
    second = time.strftime("%S")
    day = time.strftime("%A")

    my_label.config(text = hour + ":" + minute + ":" + second)
    my_label.after(1000, clock)

    my_label2.config(text=day)
    my_label2.after(86400000, clock)


my_label = Label(root, text="", font=('Helvetica', 48, ))
my_label.pack(pady=20)

my_label2 = Label(root, text="", font=('Helvetica', 14))
my_label2.pack(pady=10)

clock()

#my_label.after(5000, update)



root.mainloop()
