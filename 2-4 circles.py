import turtle

turtle.bgcolor('red')
shelly = turtle.Turtle()

for n in range(36):
    shelly.circle(100)
    shelly.right(10)

shelly.hideturtle()
