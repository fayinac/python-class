from tkinter import *
import time
import random

#setup
window = Tk()
window.title('The Spider Survival Game')

canvas = Canvas(window, width = 400, height = 400, bg = 'white')
canvas.pack()

title = canvas.create_text(200, 200, text = 'Survive the Spiders', fill = 'black', font = ('Helvetica', 30))
directions = canvas.create_text(200, 300, text = 'Avoid the spiders at all costs!', fill = 'black', font = ('Helvetica', 30))

#score
score = 0
score_display = Label(window, text = "Score: " + str(score))
score_display.pack()

#level
level = 1
level_display = Label(window, text = "Level: " + str(level))
level_display.pack()

#player
player_image = PhotoImage(file = 'stickfigure.gif')
mychar = canvas.create_image(200,360,image = player_image)


#variables for spiders
spider_list = []
spider_speed = 2

spider_image = PhotoImage(file = 'spider.gif')

def make_spider():
   xposition = random.randint(1,400)
   spider = canvas.create_image(0, xyposition, image = spider_image)
   spider_list.append(spider)
   window.after(1000, make_spider)

def move_spider():
   for spider in spider_list:
      canvas.move(spider, 0, spider_speed)
      if canvas.coords(spider)[1] > 400:
         xposition = random.randint(1,400)
         canvas.coords(spider, xposition, 0, xposition + 30, 30)
   window.after(50, move_spider)

#score update
def update_score_level():
   global score, level, spider_speed
   score = score + 1
   score_display.config(text = 'Score: ' + str(score))
   if score > 5 and score <= 10:
      spider_speed = spider_speed + 1
      level = 2
      level_display.config(text = "Level: " + str(level))
   elif score > 10:
      spider_speed = spider_speed + 1
      level = 3
      level_display.config(text = "level: " + str(level))

def end_game_over():
   window.destroy()

def end_title():
   canvas.delete(title)
   canvas.delete(directions)

#check collide
def collision(item1, item2, distance):
   xdistance = abs(canvas.coords(item1)[0] - canvas.coords(item2)[0])
   ydistance = abs(canvas.coords(item1)[1] - canvas.coords(item2)[1])
   overlap = xdistance < distance and ydistance < distance
   return overlap

def check_hits():
   for candy in spider_list:
      if collision(mychar, spider, 30):
         game_over = canvas.create_text(200, 200, text = 'Game Over', fill = 'red', font = ('Helvetica', 30))
         window.after(2000, end_game_over)
         return
   window.after(100, check_hits)

#control character with keys
move_direction = 0
def check_input(event):
   global move_direction
   key = event.keysym
   if key == "Up":
      move_direction = "Up"
   elif key == "Down":
      move_direction = "Down"
   elif key == "Right":
      move_direction = "Right"
   elif key == "Left":
      move_direction = "Left"

def end_input(event):
   global move_direction
   move_direction = "None"

def move_character():
   if move_direction == "Right" and canvas.coords(mychar)[0] < 400:
      canvas.move(mychar, 10,0)
   elif move_direction == "Left" and canvas.coords(mychar)[0] < 0:
      canvas.move(mychar, -10,0)
   elif move_direction == "Up" and canvas.coords(mychar)[1] < 0:
      canvas.move(mychar, 0,-10)
   elif move_direction == "Down" and canvas.coords(mychar)[1] < 400:
      canvas.move(mychar, 0,-10)
   window.after(16, move_character)

canvas.bind_all('<KeyPress>', check_input)
canvas.bind_all('<KeyRelease>', end_input)

#start game
window.after(1000, end_title)
window.after(1000, make_spider)
window.after(1000, move_spider)
window.after(1000, check_hits)
window.after(1000, move_character)

window.mainloop()













   



