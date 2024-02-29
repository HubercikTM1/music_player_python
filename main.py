from tkinter import filedialog
from tkinter import *
import pygame as pg
import os

root = Tk()
root.title("Hubercik Music Player")
root.geometry("600x380")

pg.mixer.init()

# menu bar
menubar = Menu(root)
root.config(menu=menubar)


songs = []
current_song = ""
paused = False

# load music
def load_music():
    global current_song
    root.directory = filedialog.askdirectory()

    for song in os.listdir(root.directory):
        name, ext = os.path.splitext(song)
        if ext == ".mp3":
            songs.append(song)

    for song in songs:
        songlist.insert("end", song)

    songlist.selection_set(0)
    current_song = songs[songlist.curselection()[0]]

# play music
def play_music():
    global current_song, paused
    if not paused:
        pg.mixer.music.load(os.path.join(root.directory, current_song))
        pg.mixer.music.play()
    else:
        pg.mixer.music.unpause()
        paused = False

# pause music
def pause_music():
    global paused
    pg.mixer.music.pause()
    paused = True

# next music
def next_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) + 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

# previous music
def previous_music():
    global current_song, paused

    try:
        songlist.selection_clear(0, END)
        songlist.selection_set(songs.index(current_song) - 1)
        current_song = songs[songlist.curselection()[0]]
        play_music()
    except:
        pass

organise_menu = Menu(menubar, tearoff=False)
organise_menu.add_command(label="Select Folder", command=load_music)
menubar.add_cascade(label="Menu", menu=organise_menu)


songlist = Listbox(root, bg="black", fg="white", width=110, height=20)
songlist.pack()

# img imports
play_btn_img = PhotoImage(file="play-btn.png")
pause_btn_img = PhotoImage(file="pause-btn.png")
next_btn_img = PhotoImage(file="next-btn.png")
previous_btn_img = PhotoImage(file="previous-btn.png")

# "div"
control_panel_frame = Frame(root)
control_panel_frame.pack()

# assign img to btn
play_btn = Button(control_panel_frame, image=play_btn_img, borderwidth=0, command=play_music)
pause_btn = Button(control_panel_frame, image=pause_btn_img, borderwidth=0, command=pause_music)
next_btn = Button(control_panel_frame, image=next_btn_img, borderwidth=0, command=next_music)
previous_btn = Button(control_panel_frame, image=previous_btn_img, borderwidth=0, command=previous_music)

play_btn.grid(row=0, column=0, padx=7, pady=10)
pause_btn.grid(row=0, column=1, padx=7, pady=10)
next_btn.grid(row=0, column=3, padx=7, pady=10)
previous_btn.grid(row=0, column=2, padx=7, pady=10)

root.mainloop()