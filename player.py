#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      vaibhav account
#
# Created:     02/11/2020
# Copyright:   (c) vaibhav account 2020
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter import *
import pygame
from tkinter import filedialog

root = Tk()
root.title('MP3')
root.geometry("500x300")

pygame.mixer.init()

#-----------------------------Functions-----------------------------------------

def add_song():
    song = filedialog.askopenfilename(initialdir='C:/songs', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))
    song = song.replace("C:/songs/", "")
    song = song.replace(".mp3", "")

    song_box.insert(END, song)

def add_many_songs():
	songs = filedialog.askopenfilenames(initialdir='audio/', title="Choose A Song", filetypes=(("mp3 Files", "*.mp3"), ))

	for song in songs:
		song = song.replace("C:/songs/", "")
		song = song.replace(".mp3", "")

		song_box.insert(END, song)

def play():
    song = song_box.get(ACTIVE)
    song = f'C:/songs/{song}.mp3'

    pygame.mixer.music.load(song)
    pygame.mixer.music.play(loops=0)

def stop():
    pygame.mixer.music.stop()
    song_box.selection_clear(ACTIVE)

global paused
paused = False

def pause(is_paused):
	global paused
	paused = is_paused

	if paused:

		pygame.mixer.music.unpause()
		paused = False
	else:

		pygame.mixer.music.pause()
		paused = True



#---------------------------User-Interface--------------------------------------

song_box = Listbox(root, bg = "Black", fg="White", width=60)
song_box.pack(pady=20)

back_btn_img = PhotoImage(file='images/back50.png')
forward_btn_img = PhotoImage(file='images/forward50.png')
play_btn_img = PhotoImage(file='images/play50.png')
pause_btn_img = PhotoImage(file='images/pause50.png')
stop_btn_img = PhotoImage(file='images/stop50.png')

controls_frame = Frame(root)
controls_frame.pack()

back_button = Button(controls_frame, image=back_btn_img, borderwidth=0)
forward_button = Button(controls_frame, image=forward_btn_img, borderwidth=0)
play_button = Button(controls_frame, image=play_btn_img, borderwidth=0, command=play)
pause_button = Button(controls_frame, image=pause_btn_img, borderwidth=0, command=lambda: pause(paused))
stop_button = Button(controls_frame, image=stop_btn_img, borderwidth=0, command = stop)

back_button.grid(row=0, column=0, padx=10)
forward_button.grid(row=0, column=1, padx=10)
play_button.grid(row=0, column=2, padx=10)
pause_button.grid(row=0, column=3, padx=10)
stop_button.grid(row=0, column=4, padx=10)

my_menu = Menu(root)
root.config(menu=my_menu)

add_song_menu = Menu(my_menu, tearoff= FALSE)
my_menu.add_cascade(label="Add Songs", menu=add_song_menu)

add_song_menu.add_command(label="Add One Song To Playlist", command = add_song)
add_song_menu.add_command(label="Add More Songs", command = add_many_songs)

root.mainloop()

