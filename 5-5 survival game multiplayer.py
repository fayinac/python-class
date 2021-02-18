from tkinter import *
import time
import random

#setup
window = Tk()
window.title('The Spider Survival Game Multiplayer')

canvas = Canvas(window, width = 400, height = 400, bg = 'white')
canvas.pack()

title = canvas.create_text(200, 200, text = 'The Spider Survival Game: 2', fill = 'black', font = ('Helvetica', 30))
directions = canvas.create_text(200, 300, text = 'Multiplayer version!', fill = 'black', font = ('Helvetica', 30))

#time
time = 0
time_display = Label(window, text = "Time: " + str(time))
time_display.pack()

#level
level = 1
level_display = Label(window, text = "Level: " + str(level))
level_display.pack()

#players
player1_image = PhotoImage(file = 'stickfigure.gif')
player2_image = PhotoImage(file = 'stickfigure.gif')
player1 = canvas.create_image(200,360,image = player1_image)
player2 = canvas.create_image(200,360,image = player2_image)


#variables for spiders
spider_list = []
spider_speed = 2

spider_image = PhotoImage(file = 'spider.gif')

def make_spider():
   xposition = random.randint(1,400)
   spider = canvas.create_image(0, xposition, image = spider_image)
   spider_list.append(spider)
   if level == 1:
      window.after(1500, make_spider)
   if level == 2:
      window.after(600, make_spider)
   if level == 3:
      window.after(300, make_spider)
      
def move_spider():
   for spider in spider_list:
      canvas.move(spider, spider_speed, 0)
   window.after(50, move_spider)

#time update
def update_time_level():
   global time, level, spider_speed
   time = time + 1
   time_display.config(text = 'Time: ' + str(time))
   if time > 15 and time <= 30:
      spider_speed = spider_speed + 1
      level = 2
      level_display.config(text = "Level: " + str(level))
   elif time > 30:
      spider_speed = spider_speed + 1
      level = 3
      level_display.config(text = "Level: " + str(level))
   window.after(1000, update_time_level)

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
   for spider in spider_list:
      if collision(player1, spider, 30):
         game_over = canvas.create_text(200, 200, text = 'Game Over', fill = 'red', font = ('Helvetica', 30))
         window.after(2000, end_game_over)
      elif collision(player2, spider, 30):
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
      move_direction = "Up1"
   elif key == "Down":
      move_direction = "Down1"
   elif key == "Right":
      move_direction = "Right1"
   elif key == "Left":
      move_direction = "Left1"
   elif key == "W":
      move_direction = "Up2"
   elif key == "S":
      move_direction = "Down2"
   elif key == "A":
      move_direction = "Right2"
   elif key == "D":
      move_direction = "Left2"

def end_input(event):
   global move_direction
   move_direction = "None"

def move_character():
   if move_direction == "Right1" and canvas.coords(player1)[0] < 400:
      canvas.move(player1, 10,0)
   elif move_direction == "Left1" and canvas.coords(player1)[0] > 0:
      canvas.move(player1, -10,0)
   elif move_direction == "Up1" and canvas.coords(player1)[1] > 0:
      canvas.move(player1, 0,-10)
   elif move_direction == "Down1" and canvas.coords(player1)[1] < 400:
      canvas.move(player1, 0,10)
   elif move_direction == "Right2" and canvas.coords(player2)[0] < 400:
      canvas.move(player2, 10,0)
   elif move_direction == "Left2" and canvas.coords(player2)[0] > 0:
      canvas.move(player2, -10,0)
   elif move_direction == "Up2" and canvas.coords(player2)[1] > 0:
      canvas.move(player2, 0,-10)
   elif move_direction == "Down2" and canvas.coords(player2)[1] < 400:
      canvas.move(player2, 0,10)
   window.after(16, move_character)


canvas.bind_all('<KeyPress>', check_input)
canvas.bind_all('<KeyRelease>', end_input)

#start game
window.after(1000, end_title)
window.after(1000, make_spider)
window.after(1000, update_time_level)
window.after(1000, move_spider)
window.after(1000, check_hits)
window.after(1000, move_character)

window.mainloop()
