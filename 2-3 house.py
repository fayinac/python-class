import turtle

turtle.bgcolor('blue')
shelly = turtle.Turtle()

shelly.begin_fill()
shelly.color('gray')
for i in range(4):
    shelly.forward(100)
    shelly.left(90)
shelly.end_fill()
shelly.penup()
shelly.goto(-20,100)
shelly.pendown

shelly.begin_fill()
shelly.color('red')
shelly.left(60)
shelly.forward(140)
shelly.right(120)
shelly.forward(140)
shelly.right(120)
shelly.forward(140)
shelly.end_fill()

shelly.penup()
shelly.goto(25,80)
shelly.pendown()
shelly.begin_fill()
shelly.color('yellow')
for i in range(4):
    shelly.forward(20)
    shelly.left(90)
shelly.end_fill()

shelly.hideturtle()
