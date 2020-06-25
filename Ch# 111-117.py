""" Reading and Writing to a .csv File """


# Ch 111
# Books.csv

import csv

file = open("Books.csv","w")
new_record = "To Kill a Mockingbird, Harper Lee, 1960\n"
file.write(str(new_record))
new_record = "A Brief History of Time, Stephen Hawking, 1988\n"
file.write(str(new_record))
new_record = "The Great Gatsby, F. Scott Fitzgerald, 1922\n"
file.write(str(new_record))
new_record = "The Man Who Mistook His Wife for a Hat, Oliver Sacks, 1985\n"
file.write(str(new_record))
new_record = "Pride and Prejudice, Jane Austen, 1813\n"
file.write(str(new_record))
file.close()


# Ch 112
import csv

file = open("Books.csv","a")
title = input("Enter a title: ")
author = input("Enter author: ")
year = input("Enter the year it was released: ")
new_record = title + ", " + author + ", " + year + "\n"
file.write(str(new_record))
file.close()

file = open("Books.csv","r")
for row in file:
    print(row)

file.close()


# Ch 113
import csv

num = int(input("How many books do you want to add to the list? "))
file = open("Books.csv","a")
for x in range(0,num):
    title = input("Enter a title: ")
    author = input("Enter author: ")
    year = input("Enter the year it was released: ")
    new_record = title + ", " + author + ", " + year + "\n"
    file.write(str(new_record))

file.close()


# Ch 114
import csv

start = int(input("Enter a starting year: "))
end = int(input("Enter an end year: "))

file = list(csv.reader(open("Books.csv")))
tmp = []
for row in file:
    tmp.append(row)

x = 0
for row in tmp:
    if int(tmp[x][2]) >= start and int(tmp[x][2]) <= end:
        print(tmp[x])
        x += 1


# Ch 115
import csv

file = open("Books.csv","r")
x = 0
for row in file:
    display = "Row: " + str(x) + " - " + row
    print(display)
    x += 1


# Ch 116
import csv

file = list(csv.reader(open("Books.csv")))
Book_list = []
for row in file:
    Book_list.append(row)

x = 0
for row in Book_list:
    display = x,Book_list[x]
    print(display)
    x += 1
get_rid = int(input("Enter a row number to delete: "))
del Book_list[get_rid]

x = 0
for row in Book_list:
    display = x,Book_list[x]
    print(display)
    x += 1
alter = int(input("Enter a row number to alter: "))
x = 0
for row in Book_list[alter]:
    display = x,Book_list[alter][x]
    print(display)
    x += 1
part = int(input("Which part do you want to change? "))
new_data = input("Enter new data: ")
Book_list[alter][part] = new_data
Book_list[alter][part] = new_data
print(Book_list[alter])

file = open("Books.csv","w")
x = 0
for row in Book_list:
    new_record = Book_list[x][0] + ", " + Book_list[x][1] + ", " + Book_list[x][2] + "\n"
    file.write(new_record)
    x += 1

file.close()


# Ch 117
import csv
import random

score = 0
name = input("What is your name? ")

# Ask question number 1
q1_num1 = random.randint(10,50)
q1_num2 = random.randint(10,50)
question1 = str(q1_num1) + " + " + str(q1_num2) + " = "
ans1 = int(input(question1))
real_ans1 = q1_num1 + q1_num2
if ans1 == real_ans1:
    score += 1

# Ask question number 2
q2_num1 = random.randint(10,50)
q2_num2 = random.randint(10,50)
question2 = str(q2_num1) + " + " + str(q2_num2) + " = "
ans2 = int(input(question2))
real_ans2 = q2_num1 + q2_num2
if ans2 == real_ans2:
    score += 1

file = open("QuizScore.csv","a")
new_record = name + ", " + question1 + ", " + str(ans1) + ", " + question2 + ", " + str(ans2) + ", " + str(score) + "\n"
file.write(str(new_record))

file.close()


