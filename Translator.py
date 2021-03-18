#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vaibhav account
#
# Created:     06/01/2021
# Copyright:   (c) vaibhav account 2021
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from translate import Translator
from tkinter import *
import webbrowser

root=Tk()
root.title("Translate app")
root.geometry('580x350')
root.configure(bg='White')

def French():
    word = E1.get()
    translator=Translator(to_lang='French')
    translation = translator.translate(word)
    l2.config(text=f'Translated word: {translation}',font=('Arial Bold',12),fg='DodgerBlue2')
    l2.place(x=5, y=180)

def german():
    word = E1.get()
    translator = Translator(to_lang='German')
    translation = translator.translate(word)
    l2.config(text=f'Translated word: {translation}', font=('Arial  Bold', 12), fg='DodgerBlue2')

def spanish():
    word = E1.get()
    translator = Translator(to_lang='Spanish')
    translation = translator.translate(word)
    l2.config(text=f'Translated word: {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')

def hindi():
    word = E1.get()
    translator = Translator(to_lang='Hindi')
    translation = translator.translate(word)
    l2.config(text=f'Translated word: {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')


def other():
    word = E1.get()
    wordd = E2.get()
    translator = Translator(to_lang=wordd)
    translation = translator.translate(word)
    l2.config(text=f'Translated word: {translation}', font=('Arial Bold', 12), fg='DodgerBlue2')

def n_w():
    webbrowser.open("https://translate.google.co.uk/")

txt=StringVar()
txts=StringVar()

l1=Label(root,text="Enter your text Here(English):", bg = "white")
l1.place(x=5,y=70)
l2=Label(root,text="Translated word:", bg = "white", font=('Arial Bold',12),fg='DodgerBlue2')
l2.place(x=5,y=270)
l3=Label(root,text="Any other language that the text should be translated to(Optional):", bg = "white")
l3.place(x=5,y=140)
l4=Label(root,text="                Translate                     ", bg = "Blue", fg = "white", font=('Product Sans', 36))
l4.place(x=0,y=0, height=60)

E1=Entry(root,textvariable=txt,width=23,font=('Arial Bold',15),bg="white")
E1.place(x=5,y=110)
E2=Entry(root,textvariable=txts,width=23,font=('Arial Bold',15),bg="white")
E2.place(x=5,y=160)

Btn1=Button(root,text='French',padx=8,pady=8,bg="SystemButtonFace",width=6,command=French)
Btn1.place(x=5,y=210)
Btn2=Button(root,text='German',padx=8,pady=8,bg="SystemButtonFace",width=6,command=german)
Btn2.place(x=75,y=210)
Btn3=Button(root,text='Spanish',padx=8,pady=8,bg="SystemButtonFace",width=6,command=spanish)
Btn3.place(x=145,y=210)
Btn4=Button(root,text='Hindi',padx=8,pady=8,bg="SystemButtonFace",width=6,command=hindi)
Btn4.place(x=215,y=210)
Btn4=Button(root,text='Other language',padx=8,pady=8,bg="SystemButtonFace",width=6,command=other)
Btn4.place(x=285,y=210, width = 100)
Btn5=Button(root,text='Not Working',padx=8,pady=8,bg="SystemButtonFace",width=6,command=n_w)
Btn5.place(x=390,y=210, width=80)

mainloop()