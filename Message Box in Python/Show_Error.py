# Show_Error.py

from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Messagebox")
top.geometry("100x100")
messagebox.showerror("Error", "This is Error!")
top.mainloop()
