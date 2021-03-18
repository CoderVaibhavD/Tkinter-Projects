#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vaibhav account
#
# Created:     04/08/2020
# Copyright:   (c) vaibhav account 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
from random import randint
from time import *
import time

root=Tk()
root.title("Random winner generator")
root.geometry('400x450')

def wait():
    winButton2 = Label(root, text="Better luck next time!", font=("Helvetica", 16))
    winButton2.pack()

def pick():
    entries = ['Aarib', 'Stan', 'Rumeth', 'DotDot', 'Daniel games', 'Tech Watcher', 'Aaryan', 'Amal', 'Technotube', 'Dad', 'Mum', 'Vaishnav', 'MrWhoseTheBoss', 'Austin Evans', 'KangarMan', 'Hanush Sittabatula']

    entries_set = set(entries)
    unique_entries = list(entries_set)

    our_number = len(unique_entries) - 1

    rando = randint(0, our_number)

    winnerLabel = Label(root, text=unique_entries[rando], font=("Helvetica", 18))
    winnerLabel.pack(pady=50)

    if pick:
        print(unique_entries[rando])

    else:
        pass

topLabel = Label(root, text="Win-O-Rama", font=("Helvetica", 24))
topLabel.pack(pady=20)

winButton = Button(root, text="PICK OUR WINNER", font=("Helvetica", 24), command=pick)
winButton.pack(pady=20)

toLabel = Button(root, text="Advice", font=("Helvetica", 12), command=wait)
toLabel.pack(pady=20)

root.mainloop()


