import turtle
import random
colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'red']
h = turtle.Turtle()
def house(x,y,wallColor,roofColor):
    h.penup()
    h.goto(x,y)
    h.setheading(0)
    h.pendown()
    h.begin_fill()
    h.color(wallColor)
    for i in range(4):
        h.right(90)
        h.forward(30)
    h.end_fill()
    h.backward(35)
    h.begin_fill()
    h.color(roofColor)
    h.left(60)
    h.forward(40)
    h.right(120)
    h.forward(40)
    h.right(120)
    h.forward(40)
    h.end_fill()

for i in range(10):
    x = random.randint(-200,200)
    y = random.randint(-200,200)
    wall = colors[random.randint(0,6)]
    roof = colors[random.randint(0,6)]
    house(x, y, wall, roof)
