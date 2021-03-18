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
import sqlite3

root=Tk()
root.title("haii")

# Database

# Create a database or connect to one.

conn = sqlite3.connect('address_book.db')

# Create cursor
c=conn.cursor()

# Create table
c.execute(""" CREATE TABLE addresses (
        first_name text,
        last_name text,
        address text,
        city text,
        state text,
        zipcode integer
        )""")

# Commit changes
conn.commit()

# Close connection
conn.close()


root.mainloop()

