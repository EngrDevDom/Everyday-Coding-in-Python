# Show_Info.py

from tkinter import *
from tkinter import messagebox

top = Tk()
top.title("Messagebox")
top.geometry("100x100")
messagebox.showinfo("Info", "This is Info!")
top.mainloop()
