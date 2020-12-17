import turtle

shelly = turtle.Turtle()

turtle.bgcolor('black')

colors = ('red', 'green', 'blue', 'orange', 'purple', 'yellow')

for n in range(6):
    for b in range(6):
        shelly.color(colors[b])
        for i in range(4):
            shelly.forward(20)
            shelly.left(90)
        shelly.penup()
        shelly.forward(30)
        shelly.pendown()
    shelly.penup()
    shelly.backward(180)
    shelly.right(90)
    shelly.forward(30)
    shelly.left(90)
    shelly.pendown()
        
