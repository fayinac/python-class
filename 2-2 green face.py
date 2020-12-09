import turtle

shelly = turtle.Turtle()

#green face
shelly.begin_fill()
shelly.color('green')
shelly.circle(105)
shelly.end_fill()

#first eye
shelly.goto(-30,100)
shelly.begin_fill()
shelly.color('white')
shelly.circle(30)
shelly.end_fill()
shelly.begin_fill()
shelly.color('black')
shelly.circle(20)
shelly.end_fill()
shelly.penup()

#second eye
shelly.goto(30,100)
shelly.pendown()
shelly.begin_fill()
shelly.color('white')
shelly.circle(30)
shelly.end_fill()
shelly.begin_fill()
shelly.color('black')
shelly.circle(20)
shelly.end_fill()

shelly.hideturtle()
