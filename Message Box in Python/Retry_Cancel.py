# Retry_Cancel.py

from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Messagebox")
top.geometry("100x100")
messagebox.askretrycancel("Ask Retry", "This is Retry Cancel")
top.mainloop()
