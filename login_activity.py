""" login_activity.py """

from tkinter import *

root = Tk()
root.title('login page')
lb1 = Label(root, text="Username", fg="green")
lb1.grid(row=0, column=0)
en1 = Text(root, width=40, height=2)
en1.grid(row=0, column=1)
lb2 = Label(root, text="Password", fg="green")
lb2.grid(row=1, column=0)
en2 = Text(root, width=40, height=2)
en2.grid(row=1, column=1)
btn = Button(root, text="Login")
btn.grid(row=2, column=0, columnspan=2)
root.mainloop()

