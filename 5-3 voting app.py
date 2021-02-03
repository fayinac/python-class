from tkinter import *

window = Tk()
window.title('Voting App')

window.configure(bg = 'black')

cat_score = dog_score = 0
int(cat_score)
int(dog_score)

top_label = Label(window, text = '', bg = "black")
top_label.pack()

def choice_cat():
   global cat_score
   cat_score = cat_score + 1
   score_display.config(text = 'Cat Lovers: ' + str(cat_score) + '\nDog Lovers: ' + str(dog_score))

def choice_dog():
   global dog_score
   dog_score = dog_score + 1
   score_display.config(text = 'Cat Lovers: ' + str(cat_score) + '\nDog Lovers: ' + str(dog_score))
   
button = Button(window, text = 'Cat Person?', compound = TOP, command = choice_cat)
button.pack()

top_label = Label(window, text = '', bg = "black")
top_label.pack()

button = Button(window, text = 'Dog Person?', compound = TOP, command = choice_dog)
button.pack()

top_label = Label(window, text = '', bg = "black")
top_label.pack()

score_display = Label(window, text = "")
score_display.pack()

window.mainloop()


