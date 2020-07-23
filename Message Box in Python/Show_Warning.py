# Show_Warning.py

from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Messagebox")
top.geometry("100x100")
messagebox.showwarning("Warning", "This is Warning!")
top.mainloop()
