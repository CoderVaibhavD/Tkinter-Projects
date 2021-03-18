    #-------------------------------------------------------------------------------
    # Name:        module1
    # Purpose:
    #
    # Author:      vaibhav account
    #
    # Created:     11/04/2020
    # Copyright:   (c) vaibhav account 2020
    # Licence:     <your licence>
    #------------------------------------------------------------------------------
import time
from datetime import date
import datetime
import webbrowser
import subprocess
import pyttsx3
import sys
import wikipedia
from tkinter import *
from PIL import ImageTk,Image

root = Tk()
root.title("UI framework")

def stop():
    sys.exit()

def cortana():
    try:
        engine = pyttsx3.init()

        engine.setProperty('rate', 165)
        engine.setProperty('volume', 10)
        voices = engine.getProperty('voices')
        engine.setProperty('voice', voices[0].id)

        engine.say("Hello, I am Cortana.\n")

        name = input("What is your name?")


        def wishMe():
            hour = int(datetime.datetime.now().hour)
            if hour>=0 and hour<12:
                engine.say("Good Morning!")
                engine.say(name)

            elif hour>=12 and hour<18:
                engine.say("Good Afternoon!")
                engine.say(name)

            else:
                engine.say("Good Evening!")
                engine.say(name)

        engine.say("Assistant mode activated\n")

        if __name__ == '__main__':
            wishMe()


            engine.runAndWait()
        engine.runAndWait()

        carryOn = True
        while True:

            j = input()
            query = j

            if "time" in query:
                print(time.strftime("%H:%M"))
                engine.say(time.strftime("%H:%M"))
                engine.say("Next command sir:")

            elif "stop" in query:
                sys.exit()

            elif "hi" in query:
                engine.say("hi")
                engine.say("Next command sir:")
                lb1=Label(root, text="hi")

            elif "calculate" in query:
                engine.say("Launching::")
                subprocess.Popen('C:\\Windows\\System32\\calc.exe')

            elif "news" in query:
                engine.say("opening bbc news")
                time.sleep(2)
                webbrowser.open('https://www.bbc.co.uk/news')
                engine.say("Next command sir:")

            elif "why" and "running" in query:
                engine.say("Because I am")

            elif "game" in query:
                engine.say("Launching google games")
                webbrowser.open('https://www.google.com/search?safe=strict&sxsrf=ALeKk01Ezw6ov7NZVLJBvcsWLZrzXEmaCg%3A1586617746287&ei=kt2RXriPEeHA8gKOiavgCg&q=snake&oq=snake&gs_lcp=CgZwc3ktYWIQAzIECCMQJzIECCMQJzIFCAAQkQIyBAgAEEMyBAgAEEMyBQgAEJECMgcIABCDARBDMgQIABBDMgQIABBDMgQIABBDOggIABCDARCRAjoFCAAQgwE6BwgAEBQQhwJKGAgXEhQwZzEyN2c3MmcxMDJnMTMyZzE3MEoPCBgSCzBnMWcxZzFnMWcxUIdcWMlnYMJqaABwAHgAgAGhAYgBogSSAQMyLjOYAQCgAQGqAQdnd3Mtd2l6&sclient=psy-ab&ved=0ahUKEwi4oKXZ0-DoAhVhoFwKHY7ECqwQ4dUDCAw&uact=5')
                engine.say("Next command sir:")

            elif "google maps" in query:
                engine.say("launching")
                engine.say("What do you want to search in google maps?")
                place = input()
                tabUrl = 'https://www.google.com/maps/search/';
                webbrowser.open(tabUrl + place)
                engine.say("Next command sir:")

            elif "name" in query:
                engine.say("My name is Cortana")

            elif "date" in query:
                today = date.today()
                engine.say(today)
                print(today)
                engine.say("Next command sir:")

            elif "youtube" in query:
                engine.say("what do you want to search in youtube?")
                q = input()
                tabUrl = 'https://www.youtube.com/results?search_query=';
                webbrowser.open(tabUrl + q)
                engine.say("Next command sir:")

            elif "wiki" in query:
                ny = input("Do you want me to show the info, say it or both?")
                engine.runAndWait()

                engine.say("What do you want to find about in wiki?")
                engine.runAndWait()

                if ny == "show":
                    ny = input("What do you want to find about in wiki?")
                    print (wikipedia.summary(ny))
                    engine.say("Next command sir:")

                elif ny == "say":
                    engine.say(wikipedia.summary(ny))
                    engine.say("Next command sir:")

                elif ny == "both":
                    print(wikipedia.summary(ny))
                    engine.say(wikipedia.summary(ny))
                    engine.say("Next command sir:")

                else:
                    engine.say("Sorry I do not understand")
                    engine.say("Next command sir:")


            elif j == "":
                engine.say(name)
                engine.say("If you do not have any questions, the command is stop.")
                engine.say("Next command sir:")

            elif "inbox" in query:
                n = input("Who's account is this?")

                if n == "school":
                    engine.say("Launching school inbox.")
                    webbrowser.open('https://outlook.office365.com/mail/inbox')
                    engine.say("Next command sir:")

                elif n == "normal":
                    engine.say("launching normal inbox")
                    webbrowser.open('https://mail.google.com/mail/u/1/?ogbl#inbox')
                    engine.say("Next command sir:")

            elif "translate" in query:
                engine.say("launching google translate")
                webbrowser.open('https://translate.google.co.uk/')
                engine.say("Next command sir:")

            elif "homeworks" in query:
                engine.say("opening google classroom")
                webbrowser.open('https://classroom.google.com/u/0/a/not-turned-in/all')
                engine.say("Next command sir:")

            elif "see world" in query:
                engine.say("opening google earth")
                webbrowser.open("https://earth.google.com/web/@0,7.658201,0a,22251752d,35y,0h,0t,0r/data=KAE")
                engine.say("Next command sir:")

            elif "measure"  in query:
                engine.say("Launching unit converter")
                webbrowser.open('https://www.unitconverters.net/')
                engine.say("Next command sir:")

            elif "call" in query:
                engine.say("Please insert a sim card")
                engine.say("Next command sir:")

            elif "message" in query:
                engine.say("Please insert a sim card")
                engine.say("Next command sir:")

            elif "remind" in query:
                engine.say("What shall I remind you about?")
                text = str(input("What shall I remind you about?"))
                engine.say("In how many minutes?")
                local_time = float(input("In how many minutes?"))
                local_time = local_time * 60
                time.sleep(local_time)
                engine.say(text)
                engine.say("Next command sir:")

            elif "passwords" in query:
                engine.say("Sorry, I cannot do that because of security reasons")
                engine.say("Next command sir:")

            elif "Thank you" in query:
                engine.say("I am always there for you!")
                engine.say("Next command sir:")

            elif "friend" in query:
                engine.say("You!")
                engine.say(name)
                engine.say("Next command sir:")

            elif "Hey" in query:
                engine.say(name)
                engine.say("What can I do for you?")

            elif "notepad" in query:
                engine.say("Opening notepad")
                subprocess.Popen('C:\\Windows\\System32\\notepad.exe')

            elif "snapchat" in query:
                engine.say("no")

            elif "instagram"in query:
                engine.say("no")

            elif "what do you have" in query:
                engine.say("A BRAIN")

            else:
                engine.say("Opening result in google.")
                tabUrl = 'https://www.google.com/search?q=';
                webbrowser.open_new_tab(tabUrl + j)
                engine.say("Next command sir:")



            engine.runAndWait()
        engine.runAndWait()

    except:
        engine.say('Cortana has stopped')
        engine.runAndWait()

btn=Button(root, text="Initiate cortana", command=cortana).pack()
btn2=Button(root, text="Stop Cortana", command=stop).pack()

try:
    my_img = ImageTk.PhotoImage(Image.open("Z:\Cortana.jpg"))
    my_label = Label(image=my_img)
    my_label.pack()
except:
    pass

root.mainloop()