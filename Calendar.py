#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vaibhav account
#
# Created:     31/07/2020
# Copyright:   (c) vaibhav account 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
import calendar

root = Tk()
root.title('Hi')
root.geometry('240x200')

def show():
    a = int(spin1.get())
    b = int(spin2.get())

    cal = calendar.month(b, a)


    txt.delete(0.0, END)
    txt.insert(INSERT, cal)


lbl1 = Label(root, text="Month", font=('helvetica', 9)).place(x=15, y=0)

lbl2 = Label(root, text="Year", font=('helvetica', 9)).place(x=115, y=0)

spin1 = Spinbox(root, values=(1,2,3,4,5,6,7,8,9,10,11,12), width=4)
spin1.place(x=60, y=0)

spin2 = Spinbox(root, values=1999, to= 2100, width=4)
spin2.place(x=150, y=0)

btn = Button (root, text="show", font=('arial', 9), command=show).place(x=100, y=30)

txt=Text(root, width=24, height=8)
txt.place(x=20, y=57)

mainloop()
