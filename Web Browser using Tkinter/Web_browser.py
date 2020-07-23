# Create Web Browser using Tkinter

import tkinter as tk
from tkinter import *
import webbrowser

top = tk.Tk()
top.title("Web Browser")
top.geometry("250x250")
top.iconbitmap("wiki.ico")

def google():
    webbrowser.open("www.google.com")

def youtube():
    webbrowser.open("www.youtube.com")

def twitter():
    webbrowser.open("www.twitter.com")

def facebook():
    webbrowser.open("www.facebook.com")

icongoogle = PhotoImage(file="google.png")
google = tk.Button(top, image=icongoogle, command=google)
google.grid(row=0, column=0)

iconyoutube = PhotoImage(file="youtube.png")
youtube = tk.Button(top, image=iconyoutube, command=youtube)
youtube.grid(row=0, column=1)

icontwitter = PhotoImage(file="twitter.png")
twitter = tk.Button(top, image=icontwitter, command=twitter)
twitter.grid(row=1, column=0)

iconfacebook = PhotoImage(file="facebook.png")
facebook = tk.Button(top, image=iconfacebook, command=facebook)
facebook.grid(row=0, column=1)

top.mainloop()
