""" More Tkinter """


# Ch 133

from tkinter import *

def click():
    name = textbox1.get()
    message = str("Hello " + name)
    textbox2["text"] = message

window = Tk()
window.title("Names")
window.geometry("450x350")
window.wm_iconbitmap("stripes.ico")
window.configure(background = "black")

logo = PhotoImage(file = "Mylogo.gif")
logo_image = Label(image = logo)
logo_image.place(x = 100, y = 20, width = 200, height = 150)

label1 = Label(text = "Enter your name: ")
label1.place(x = 30, y = 200)
label1["bg"] = "black"
label1["fg"] = "white"

textbox1 = Entry(text = "")
textbox1.place(x = 150, y = 200, width = 200, height = 25)
textbox1["justify"] = "center"
textbox1.focus()

button1 = Button(text = "Press me", command = click)
button1.place(x = 30, y = 250, width = 200, height = 25)
textbox2["bg"] = "white"
textbox2["fg"] = "black"

window.mainloop()


# Ch 134

from tkinter import *
import random

def check_ans():
    their_ans = ans_box.get()
    their_ans = int(their_ans)
    num1 = num1_box["text"]
    num2 = int(num1)
    num2 = num2_box["text"]
    num2 = int(num2)
    ans = num1 + num2
    if their_ans == ans:
        img = PhotoImage(file = "correct.gif")
        imgbx.image = img
    else:
        img = PhotoImage(file = "wrong.gif")
        imgbx.image = img
    imgbx["image"] = img
    imgbx.update()

def next_question():
    ans_box.delete(0,END)
    num1 = random.randint(10,50)
    num1_box["text"] = num1
    num2 = random.randint(10,50)
    num2_box["text"] = num2
    img = PhotoImage(file = "")
    imgbx.image = img
    imgbx["image"] = img
    imgbx.update()

window = Tk()
window.title("Addition")
window.geometry("250x300")

num1_box = Label(text = "0")
num1_box.place(x = 50, y = 30, width = 25, height = 25)
addsymbl = Message(text = "+")
addsymbl.place(x = 75, y = 30, width = 25, height = 25)
num2_box = Label(text = "0")
num2_box.place(x = 100, y = 30, width = 25, height = 25)
eqlsymbl = Message(text = "")
eqlsymbl.place(x = 125, y = 30, width = 25, height = 25)
ans_box = Entry(text = "")
ans_box.place(x = 150, y = 30, width = 25, height = 25)
ans_box["justify"] = "center"
ans_box.focus()
check_btn = Button(text = "Check", command = check_ans)
check_btn.place(x = 50, y = 60, width = 75, height = 25)
next_btn = Button(text = "Next", command = next_question)
next_btn.place(x = 130, y = 60, width = 75, height = 25)
img = PhotoImage(file = "")
imgbx = Label(image = img)
imgbx.image = img
imgbx.place(x = 25, y = 100, width = 200, height = 150)

next_question()

window.mainloop()


# Ch 135

from tkinter import *

def clicked():
    sel = select_color.get()
    window.configure(background = sel)

window = Tk()
window.title("background")
window.geometry("200x200")

select_color = StringVar(window)
select_color.set("Grey")

color_list = OptionMenu(window, select_color, "Grey", "Red", "Blue", "Green", "Yellow")
color_list.place(x = 50, y = 30)

click_me = Button(text = "Click Me", command = clicked)
click_me.place(x = 50, y = 150, width = 60, height = 30)

mainloop()


# Ch 136

from tkinter import *

def add_to_list():
    name = namebox.get()
    namebox.delete(0,END)
    gender_selection = gender.get()
    gender.set("M/F")
    new_data = name + ", " + gender_selection + "\n"
    name_list.insert(END,new_data)
    namebox.focus()

window = Tk()
window.title("People List")
window.geometry("400x400")

namelbl = Label(text = "Enter their name: ")
namelbl.place(x = 50, y = 50, width = 100, height = 25)
namebox = Entry(text = "")
namebox.place(x = 150, y = 50, width = 150, height = 25)
namebox.focus()

genderlbl = Label(text = "Select_Gender")
genderlbl.place(x = 50, y = 100, width = 100, height = 25)
gender = StringVar(window)
gender.set("M/F")
gender_menu = OptionMenu(window, gender, "M", "F")
gender_menu.place(x = 150, y = 100)

name_list = Listbox()
name_list.place(x = 150, y = 150, width = 150, height = 100)

add_btn = Button(text = "Add to List", command = add_to_list)
add_btn.place(x = 50, y = 300, width = 100, height = 25)

window.mainloop()


# Ch 137

from tkinter import *

def add_to_list():
    name = namebox.get()
    namebox.delete(0,END)
    gender_selection = gender.get()
    gender.set("M/F")
    new_data = name + ", " + gender_selection + "\n"
    name_list.insert(END,new_data)
    namebox.focus()
    file = open("names.txt","a")
    file.write(new_data)
    file.close()

def print_list():
    file = open("names.txt","r")
    print(file.read())

window = Tk()
window.title("People List")
window.geometry("400x400")

namelbl = Label(text = "Enter their name: ")
namelbl.place(x = 50, y = 50, width = 100, height = 25)
namebox = Entry(text = "")
namebox.place(x = 150, y = 50, width = 150, height = 25)
namebox.focus()

genderlbl = Label(text = "Select Gender")
genderlbl.place(x = 50, y = 100, width = 100, height = 25)
gender = StringVar(window)
gender.set("M/F")
gendermenu = OptionMenu(window, gender, "M", "F")
gendermenu.place(x = 150, y = 100)

name_list = Listbox()
name_list.place(x = 150, y = 300, width = 100, height = 25)

printlst = Button(text = "Print List", command = print_list)
printlst.place(x = 175, y = 300, width = 100, height = 25)

window.mainloop()


# Ch 138

from tkinter import *

def clicked():
    num = selection.get()
    artref = num + ".gif"
    photo = PhotoImage(file = artref)
    photobox.image = photo
    photobox["image"] = photo
    photobox.update()

window = Tk()
window.title("Art")
window.geometry("400x350")

art = PhotoImage(file = "1.gif")
photobox = Label(window, image = art)
photobox.image = art
photobox.place(x = 100, y = 20, width = 200, height = 150)

label = Label(text = "Select Art number: ")
label.place(x = 50, y = 200, width = 100, height = 25)

selection = Entry(text = "")
selection.place(x = 200, y = 200, width = 100, height = 25)
selection.focus()

button = Button(text = "See Art", command = clicked)
button.place(x = 150, y = 250, width = 100, height = 25)

window.mainloop()

