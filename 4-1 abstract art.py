import turtle
import random
colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow', 'red']
h = turtle.Turtle()

for n in range(100):
    h.forward(random.randint(0,100))
    h.begin_fill()
    h.color(colors[random.randint(0,6)])
    s = random.randint(0,100)
    h.left(90)
    h.forward(s)
    h.right(90)
    h.forward(s)
    h.right(90)
    h.forward(s)
    h.right(90)
    h.forward(s)
    h.end_fill()
    s = random.randint(0,100)
    h.forward(random.randint(20,100))
    h.left(random.randint(0,360))
    h.begin_fill()
    h.color(colors[random.randint(0,6)])
    h.left(60)
    h.forward(s)
    h.right(120)
    h.forward(s)
    h.right(120)
    h.forward(s)
    h.end_fill()
    
    
    
