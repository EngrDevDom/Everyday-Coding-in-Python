""" Tkinter GUI """


# Ch 124
from tkinter import *

def Click():
    name = textbox1.get()
    message = str("Hello " + name)
    textbox1["bg"] = "yellow"
    textbox1["fg"] = "blue"
    textbox1["text"] = message

window = Tk()
window.geometry("500x200")

label1 = Label(text = "Enter your name: ")
label1.place(x = 30, y = 20)

textbox1 = Entry(text = "")
textbox1.place(x = 150, y = 20, width = 200, height = 25)
textbox1["justify"] = "center"
textbox1.focus()

button1 = Button(text = "Press me", command = Click)
button1.place(x = 30, y = 50, width = 120, height = 25)

textbox2 = Message(text = "")
textbox2.place(x = 150, y = 50, width = 200, height = 25)
textbox2["bg"] = "white"
textbox2["fg"] = "black"

window.mainloop()


# Ch 125
from tkinter import *
import random

def Click():
    num = random.randint(1,6)
    answer["text"] = num

window = Tk()
window.title("Roll a dice")
window.geometry("100x120")

button1 = Button(text = "Roll", command = Click)
button1.place(x = 30, y = 30, width = 50, height = 50)

answer = Message(text = "")
answer.place(x = 40, y = 70, width = 30, height = 25)

window.mainloop()


# Ch 126
from tkinter import *

def Add_On():
    num = enter_txt.get()
    num = int(num)
    answer = output_txt["text"]
    answer = int(answer)
    total = num + answer
    output_txt["text"] = total

def Reset():
    total = 0
    output_txt["text"] = 0
    enter_txt.delete(0, END)
    enter_txt.focus()

total = 0
num = 0

window = Tk()
window.title("Adding Together")
window.geometry("450x100")

enter_lbl = Label(text = "Enter a number: ")
enter_lbl.place(x = 50, y = 20, width = 100, height = 25)

enter_txt = Entry(text = 0)
enter_txt.place(x = 150, y = 20, width = 100, height = 25)
enter_txt["justify"] = "center"
enter_txt.focus()

add_btn = Button(text = "Add", command = Add_On)
add_btn.place(x = 300, y = 20, width = 50, height = 25)

output_lbl = Label(text = "Answer = ")
output_lbl.place(x = 50, y = 50, width = 100, height = 25)

output_txt = Message(text = 0)
output_txt.place(x = 150, y = 50, width = 100, height = 25)
output_txt["bg"] = "white"
output_txt["relief"] = "sunken"

clear_btn = Button(text = "Clear", command = Reset)
clear_btn.place(x = 300, y = 50, width = 50, height = 25)

window.mainloop()


# Ch 127
from tkinter import *

def Add_Name():
    name = name_box.get()
    name_list.insert(END,name)
    name_box.delete(0,END)
    name_box.focus()

def Clear_List():
    name_list.delete(0,END)
    name_box.focus()

window = Tk()
window.title("Names list")
window.geometry("400x200")

label1 = Label(text = "Enter a name: ")
label1.place(x = 20, y = 20, width = 100, height = 25)

name_box = Entry(text = 0)
name_box.place(x = 120, y = 20, width = 100, height = 25)
name_box.focus

button1 = Button(text = "Add to list", command = Add_Name)
button1.place(x = 250, y = 20, width = 100, height = 25)

name_list = Listbox()
name_list.place(x = 120, y = 50, width = 100, height = 100)

button2 = Button(text = "Clear list", command = Clear_List)
button2.place(x = 250, y = 50, width = 100, height = 25)

window.mainloop()


# Ch 128
# Kilometer to Mile conversion
from tkinter import *

def convert2():
    km = textbox1.get()
    km = int(km)
    message = km * 0.6214
    textbox2.delete(0,END)
    textbox2.insert(END,message)
    textbox2.insert(END,"miles")

window = Tk()
window.title("Distance")
window.geometry("260x200")

label1 = Label(text = "Enter the value you want to convert: ")
label1.place(x = 30, y = 20)

textbox1 = Entry(text = "")
textbox1.place(x = 30, y = 50, width = 50, height = 25)
textbox1["justify"] = "center"
textbox1.focus()

convert1 = Button(text = "Convert miles to km", command = convert1)
convert1.place(x = 30, y = 80, width = 200, height = 25)

convert2 = Button(text = "Convert km to mile", command = convert2)
convert2.place(x = 30, y = 110, width = 200, height = 25)

textbox2 = Entry(text = "")
textbox2.place(x = 30, y = 140, width = 200, height = 25)
textbox2["justify"] = center

window.mainloop()


# Ch 129
from tkinter import *

def add_number():
    num = num_box.get()
    if num.isdigit():
        num_list.insert(END,num)
        num_box.delete(0,END)
        num_box.focus()
    else:
        num_box.delete(0,END)
        num_box.focus()

def clear_list():
    num_list.delete(0,END)
    num_box.focus()

window = Tk()
window.title("Number list")
window.geometry("400x200")

label1 = Label(text = "Enter a number: ")
label1.place(x = 20, y = 20, width = 100, height = 25)

num_box = Entry(text = 0)
num_box.place(x = 120, y = 20, width = 100, height = 25)
num_box.focus()

button1 = Button(text = "Add to list", command = add_number)
button1.place(x = 250, y = 20, width = 100, height = 25)

num_list = Listbox()
num_list.place(x = 120, y = 50, width = 100, height = 100)

button2 = Button(text = "Clear list", command = clear_list)
button2.place(x = 250, y = 50, width = 100, height = 25)

window.mainloop()


# Ch 130
from tkinter import *
import csv

def add_number():
    num = num_box.get()
    if num.isdigit():
        num_list.insert(END,num)
        num_box.delete(0,END)
        num_box.focus()
    else:
        num_box.delete(0,END)
        num_box.focus()

def clear_list():
    num_list.delete(0,END)
    num_box.focus()

def save_list():
    file = open("numbers.csv","w")
    tmp_list = num_list(0,END)
    item = 0
    for x in tmp_list:
        new_record = tmp_list[item] + "\n"
        file.write(str(new_record))
        item += 1
    file.close()

window = Tk()
window.title("Number list")
window.geometry("400x200")

label1 = Label(text = "Enter a number: ")
label1.place(x = 20, y = 20, width = 100, height = 25)

num_box = Entry(text = 0)
num_box.place(x = 120, y = 20, width = 100, height = 25)
num_box.focus()

button1 = Button(text = "Add to list", command = add_number)
button1.place(x = 250, y = 20, width = 100, height = 25)

num_list = Listbox()
num_list.place(x = 120, y = 50, width = 50, height = 100)

button2 = Button(text = "Clear list", command = clear_list)
button2.place(x = 250, y = 50, width = 100, height = 25)

button3 = Button(text = "Save list", command = save_list)
button3.place(x = 250, y = 50, width = 100, height = 25)

window.mainloop()


# Ch 131
from tkinter import *
import csv

def create_new():
    file = open("ages.csv","w")
    file.close()

def save_list():
    file = open("ages.csv","a")
    name = name_box.get()
    age = age_box.get()
    new_record = name + ", " + age + "\n"
    file.write(str(new_record))
    file.close()
    name_box.delete(0,END)
    age_box.delete(0,END)
    name_box.focus()

window = Tk()
window.title("People List")
window.geometry("400x100")

label1 = Label(text = "Enter a name: ")
label1.place(x = 20, y = 20, width = 100, height = 25)

name_box = Entry(text = "")
name_box.place(x = 120, y = 20, width = 100, height = 25)
name_box["justify"] = "left"
name_box.focus()

label2 = Label(text = "Enter their age: ")
label2.place(x = 20, y = 50, width = 100, height = 25)

age_box = Entry(text = "")
age_box.place(x = 120, y = 50, width = 100, height = 25)
age_box["justify"] = "left"

button1 = Button(text = "Create new file", command = create_new)
button1.place(x = 250, y = 20, width = 100, height = 25)

button2 = Button(text = "Create new file", command = create_new)
button2.place(x = 250, y = 50, width = 100, height = 25)

window.mainloop()


# Ch 132
from tkinter import *
import csv

def save_list():
    file = open("ages.csv","a")
    name = name_box.get()
    age = age_box.get()
    new_record = name + ", " + age + "\n"
    file.write(str(new_record))
    file.close()
    name_box.delete(0,END)
    age_box.delete(0,END)
    name_box.focus()

def read_list():
    name_list.delete(0,END)
    file = list(csv.reader(open("ages.csv")))
    tmp = []
    for row in file:
        tmp.append(row)
    x = 0
    for i in tmp:
        data = tmp[x]
        name_list.insert(END,data)
        x += 1

window = Tk()
window.title("People List")
window.geometry("400x200")

label1 = Label(text = "Enter a name: ")
label1.place(x = 20, y = 20, width = 100, height = 25)

name_box = Entry(text = "")
name_box.place(x = 120, y = 20, width = 100, height = 25)
name_box["justify"] = "left"
name_box.focus()

label2 = Label(text = "Enter their age: ")
label2.place(x = 20, y = 50, width = 100, height = 25)

age_box = Entry(text = "")
age_box.place(x = 120, y = 50, width = 100, height = 25)
age_box["justify"] = "left"

button1 = Button(text = "Add to file", command = save_list)
button1.place(x = 250, y = 20, width = 100, height = 25)

button2 = Button(text = "Read list", command = read_list)
button2.place(x = 250, y = 50, width = 100, height = 25)

label3 = Label(text = "Saved Names:")
label3.place(x = 20, y = 80, width = 100, height = 25)

window.mainloop()

