"""" SQLite """


# Ch 139
import sqlite3

with sqlite3.connect("Phonebook.db") as db:
    cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Names(id integer PRIMARY KEY,firstname text, surname text, phonenumber text); """)
cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber) VALUES("1", "Simon", "Howels", "0123 349752") """)
db.commit()
cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber) VALUES("2", "Karen", "Phillips", "01954 295773") """)
db.commit()
cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber) VALUES("3", "Darren", "Smith", "01583 749012") """)
db.commit()
cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber) VALUES("4", "Anne", "Jones", "01323 567322") """)
db.commit()
cursor.execute(""" INSERT INTO Names(id, firstname, surname, phonenumber) VALUES("5", "Mark", "Smith", "01223 85534") """)
db.commit()

db.close()


# Ch 140
import sqlite3

def viewphonebook():
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)

def addtophonebook():
    newid = int(input("Enter ID: "))
    newfname = input("Enter first name: ")
    newsname = input("Enter surname: ")
    newpnum = input("Enter phone number: ")
    cursor.execute(""" INSERT INTO Names (id, firstname, surname, phonenumber) VALUES (?,?,?,?) """, (newid, newfname, newsname, newpnum))
    db.commit()

def selectname():
    selectsurname = input("Enter a surname: ")
    cursor.execute("SELECT * FROM Names WHERE surname = ?", [selectname])
    for x in cursor.fetchall():
        print(x)

def deletedata():
    selectid = int(input("Enter ID: "))
    cursor.execute("DELETE FROM Names WHERE id = ?", [selectid])
    cursor.execute("SELECT * FROM Names")
    for x in cursor.fetchall():
        print(x)
    db.commit()

with sqlite3.connect("Phonebook.db") as db:
    cursor = db.cursor()

def main():
    again = "y"
    while again == "y":
        print()
        print("Main Menu")
        print()
        print("1) View phone book")
        print("2) Add to phone book")
        print("3) Search for surname")
        print("4) Delete person from phone book")
        print("5) Quit")
        print()
        selection = int(input("Enter your selection: "))
        print()

        if selection == 1:
            viewphonebook()
        elif selection == 2:
            addtophonebook()
        elif selection == 3:
            selectname()
        elif selection == 4:
            deletedata()
        elif selection == 5:
            again == "n"
        else:
            print("Incorrect selection entered")

main()
db.close()


# Ch 141
import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Authors (Name text PRIMARY KEY, PlaceofBirth text); """)
cursor.execute(""" INSERT INTO Authors(Name, PlaceofBirth) VALUES ("Agatha Christie", "Torquay") """)
db.commit()
cursor.execute(""" INSERT INTO Authors(Name, PlaceofBirth) VALUES("Cecelia Ahern", "Dublin") """)
db.commit()
cursor.execute(""" INSERT INTO Authors(Name, PlaceofBirth) VALUES("J.K. Rowling", "Bristol") """)
db.commit()
cursor.execute(""" INSERT INTO Authors(Name, PlaceofBirth) VALUES("Oscar Wilde", "Dublin") """)
db.commit()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Books (ID integer, PRIMARY KEY, Title text, Author text, DatePublished integer); """)
cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished) VALLUES("1", "De Profundis", "Oscar Wilde", "1905") """)
db.commit()
cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished) VALLUES("2", "Harry Potter and the chamber of secrets", "J.K. Rowling", "1905") """)
db.commit()
cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished) VALLUES("3", "Harry Potter and the prisoner of Azkaban", "", "1905") """)
db.commit()
cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished) VALLUES("4", "Lyrebird", "Cecilia Ahern", "1905") """)
db.commit()
cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished) VALLUES("5", "Murder of the Orient Express", "Agatha Christie", "1905") """)
db.commit()
cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished) VALLUES("6", "Perfect", "Cecilia Ahern", "1905") """)
db.commit()
cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished) VALLUES("7", "The marble collector", "Cecilia Ahern", "1905") """)
db.commit()
cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished) VALLUES("8", "The murder on the links", "Agatha Christie", "1905") """)
db.commit()
cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished) VALLUES("9", "The picture of Dorian Gray", "Oscar Wilde", "1905") """)
db.commit()
cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished) VALLUES("10", "The secret adversary", "Agatha Christie", "1905") """)
db.commit()
cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished) VALLUES("11", "The seven dials mystery", "Agatha Christie", "1905") """)
db.commit()
cursor.execute(""" INSERT INTO Books(ID, Title, Author, DatePublished) VALLUES("12", "The year I met you", "Cecilia Ahern", "1905") """)
db.commit()

db.close()


# Ch 142
import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT * FROM Authors")
for x in cursor.fetchall():
    print(x)

print()
location = input("Enter a place of birth: ")
print()

cursor.execute(
    """ SELECT Books.Title, Books.DatePublished, Books.Author FROM Books, Authors WHERE Authors.Name = Books.Author AND Authors.PlaceofBirth = ? """,
    [loacation])
for x in cursor.fetchall():
    print(x)

db.close()


# Ch 143
import sqlite3

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

selectionyear = int(input("Enter a year: "))
print()

cursor.execute(
    """ SELECT Books.Title, Books.DatePublished, Books.Author, FROM Books WHERE DatePublished = ?  ORDER BY DatePublished """,
    [selectionyear])
for x in cursor.fetchall():
    print(x)

db.close()

# Ch 144
import sqlite3

file = open("BooksList.txt", "w")

with sqlite3.connect("BookInfo.db") as db:
    cursor = db.cursor()

cursor.execute("SELECT Name from Authors")
for x in cursor.fetchall():
    print(x)

print()
selectauthor = input("Enter an author's name: ")
print()

cursor.execute("SELECT * FROM Books WHERE Author = ?", [selectauthor])
for x in cursor.fetchall():
    newrecord = str(x[0]) + " - " + x[1] + " - " + x[2] + " - " + str(x[3]) + "\n"
    file.write(newrecord)

file.close()

db.close()


# Ch 145
import sqlite3
from tkinter import *

def addtolist():
    newname = sname.get()
    newgrade = sgrade.get()
    cursor.execute(""" INSERT INTO Scores (name, score) VALUES (?,?) """, (newname, newgrade))
    db.commit()
    sname.delete(0,END)
    sgrade.delete(0,END)
    sname.focus()

def clearlist():
    sname.delete(0,END)
    sgrade.delete(0,END)
    sname.focus()

with sqlite3.connect("TestScore.db") as db:
    cursor = db.cursor()

cursor.execute(""" CREATE TABLE IF NOT EXISTS Scores(id integer PRIMARY KEY, name text, score integer); """)

window = Tk()
window.title("TestScores")
window.geometry("450x200")

label1 = Label(text = "Enter student's name: ")
label1.place(x = 30, y = 35)

sname = Entry(text = "")
sname.place(x = 150, y = 35, width = 200, height = 25)
sname.focus()

label2 = Label(text = "Enter student's grade: ")
label2.place(x = 30, y = 80)

sgrade = Entry(text = "")
sgrade.place(x = 150, y = 80, width = 200, height = 25)
sgrade.focus()


addbtn = Button(text = "Add", command = addtolist)
addbtn.place(x = 150, y = 120, width = 75, height = 25)

clearbtn = Button(text = "Clear", command = clearlist)
clearbtn.place(x = 250, y = 120, width = 75, height = 25)

window.mainloop()
db.close()

