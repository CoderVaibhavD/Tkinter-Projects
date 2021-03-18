#===============================================================================
# Name:         Notepad
# Purpose:      Replica of windows notepad
#
# Author:      Vaibhav Dachavaram
#
# Created:     22/08/2020
# Copyright:   (c) vaibhav account 2020
# Licence:     <Vaibhav Dachavaram>
#===============================================================================
from tkinter import *
from tkinter import filedialog
from tkinter import font
from tkinter import colorchooser
from tkinter import messagebox
from tkinter import ttk

#===============================================================================

import subprocess
import random
import os, sys
import sys
import time
import pyttsx3
import webbrowser as google
import pygame
import sqlite3

#===============================================================================

window=Tk()

#===============================================================================

def login():
	def login_database():
		conn=sqlite3.connect("login.db")
		cur=conn.cursor()
		cur.execute("SELECT * FROM test WHERE name=? AND password=?",(e1.get(),e2.get()))
		row=cur.fetchall()
		conn.close()
		if row!=[]:
			import notepad_logic

		else:
			messagebox.showerror("Wrong", "Wrong details. Try again.")



	window.destroy()
	login_window=Tk()
	login_window.geometry("285x200")
	l1=Label(login_window,text="username",font="times 20")
	l1.grid(row=1,column=1)
	l2=Label(login_window,text="password",font="times 20")
	l2.grid(row=2,column=1)
	l3=Label(login_window,font="times 20")
	l3.grid(row=5,column=2)

	email_text=StringVar()
	e1=Entry(login_window,textvariable=email_text)
	e1.grid(row=1,column=2)
	password_text=StringVar()
	e2=Entry(login_window,textvariable=password_text, show="●")
	e2.grid(row=2,column=2)


	b1=Button(login_window,text="login",width=20,command=login_database)
	b1.grid(row=4,column=2)
	login_window.mainloop()

#===============================================================================
def signup():
	def signup_database():
		conn=sqlite3.connect("login.db")
		cur=conn.cursor()
		cur.execute("CREATE TABLE IF NOT EXISTS test(id INTEGER PRIMARY KEY,name text,email text, password text)")
		cur.execute("INSERT INTO test Values(Null,?,?,?)",(e1.get(),e2.get(),e3.get()))
		l4=Label(signup_window,text="account created",font="times 15")
		l4.grid(row=6,column=2)
		conn.commit()
		conn.close()


	window.destroy()
	signup_window=Tk()
	signup_window.geometry("350x180")
	l1=Label(signup_window,text="user username",font="times 20")
	l1.grid(row=1,column=1)
	l2=Label(signup_window,text="user email      ",font="times 20")
	l2.grid(row=2,column=1)
	l3=Label(signup_window,text="user password",font="times 20")
	l3.grid(row=3,column=1)


	name_text=StringVar()
	e1=Entry(signup_window,textvariable=name_text)
	e1.grid(row=1,column=2)
	email_text=StringVar()
	e2=Entry(signup_window,textvariable=email_text)
	e2.grid(row=2,column=2)
	password_text=StringVar()
	e3=Entry(signup_window,textvariable=password_text)
	e3.grid(row=3,column=2)

	b1=Button(signup_window,text="login",width=20,command=signup_database)
	b1.grid(row=4,column=2)

l1=Label(window,text="what do you want to do",font="times 20")
l1.grid(row=1,column=2,columnspan=2)

b1=Button(window,text="login",width=20,command=login)
b1.grid(row=2,column=2)

b2=Button(window,text="signup",width=20,command=signup)
b2.grid(row=2,column=3)

#===============================================================================
def on_closing():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        window.destroy()

window.protocol("WM_DELETE_WINDOW", on_closing)
window.mainloop()