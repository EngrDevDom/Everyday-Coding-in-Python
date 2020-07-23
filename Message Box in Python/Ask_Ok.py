# Ask_Ok.py

from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Messagebox")
top.geometry("100x100")
messagebox.askokcancel("Ask", "This is Ask Ok!")
top.mainloop()
