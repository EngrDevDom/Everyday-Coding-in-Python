# Yes_No.py

from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Messagebox")
top.geometry("100x100")
messagebox.askyesno("Ask", "This is Yes/No!")
top.mainloop()
