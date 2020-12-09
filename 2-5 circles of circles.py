import turtle

turtle.bgcolor('black')
shelly = turtle.Turtle()

shelly.color('white')

for n in range(36):
    shelly.penup()
    shelly.forward(200)
    for i in range(6):
        shelly.pendown()
        shelly.circle(5)
        shelly.penup()
        shelly.backward(20)
    shelly.backward(80)
    shelly.right(10)

shelly.hideturtle()
    
        
