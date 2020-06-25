# Ch 60
# Draw a Square
import turtle

for i in range(0,4):
    turtle.forward(100)
    turtle.right(90)
turtle.exitonclick()

# Ch 61
# Draw a Triangle
import turtle

for i in range(0,3):
    turtle.forward(100)
    turtle.left(120)
turtle.exitonclick()

# Ch 62
# Draw a Circle
import turtle

for i in range(0,360):
    turtle.forward(1)
    turtle.right(1)
turtle.exitonclick()

# Ch 63
# Draw a three box with three different colors.
import turtle

turtle.color("black", "red")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "yellow")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.penup()
turtle.end_fill()
turtle.forward(100)

turtle.pendown()
turtle.color("black", "orange")
turtle.begin_fill()
for i in range(0,4):
    turtle.forward(70)
    turtle.right(90)
turtle.end_fill()

turtle.exitonclick()

# Ch 64
# Draw a five pointed star.
import turtle

for i in range(0,5):
    turtle.forward(100)
    turtle.right(144)
turtle.exitonclick()

# Ch 65
# Write numbers 1, 2, and 3.
import turtle

turtle.left(90)
turtle.forward(100)
turtle.right(90)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(75)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)
turtle.penup()
turtle.forward(50)
turtle.pendown()
turtle.forward(75)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(45)
turtle.left(180)
turtle.forward(45)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(75)

turtle.hideturtle()

turtle.exitonclick()

# Ch 66
# Draw an octagon that uses different random colors.
import turtle
import random

turtle.pensize(3)

for i in range(0,8):
    turtle.color(random.choice(["red", "blue", "yellow", "green", "pink", "orange"]))
    turtle.forward(50)
    turtle.right(45)
turtle.exitonclick()

# Ch 67
import turtle
import random

for x in range(0,10):
    for i in range(0,8):
        turtle.forward(50)
        turtle.right(45)
    turtle.right(36)

turtle.hideturtle()
turtle.exitonclick()

# Ch 68
# A pattern that change each time the program is run.
import turtle
import random

lines = random.randint(5,20)

for x in range(0,lines):
    length = random.randint(25,100)
    rotate = random.randint(1,365)
    turtle.forward(length)
    turtle.right(rotate)

turtle.exitonclick()
