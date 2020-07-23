# Ask_Question.py

from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Messagebox")
top.geometry("100x100")
messagebox.askquestion("Ask Question", "This is Question!")
top.mainloop()
