import turtle

jack = turtle.Turtle()
jack.color("yellow")
jack.speed(20)

def draw_square():
    for square in range(4):
        jack.forward(100)
        jack.right(90)

jack.penup()
jack.back(150)
jack.pendown()

draw_square()
jack.forward(100)
draw_square()
jack.forward(100)
draw_square()

for square in range(80):
    draw_square()
    jack.forward(5)
    jack.left(5)
