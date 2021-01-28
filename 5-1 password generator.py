import random
from tkinter import *

commonWords = ['cat', 'dog', 'jump', 'train', 'toast', 'love', 'water', 'phone', 'bread']
specialChars = ['!', '%', '&', '$']

password = random.choice(commonWords) + random.choice(specialChars) + random.choice(commonWords) + str(random.randint(0,100)) + random.choice(specialChars)

window = Tk()
window.title('Password Generator')

def password_generator():
   print(password)
   display_area.config(text = password, fg = 'black', bg = 'white')

button1 = Button(window, text = 'Generate Password', command = password_generator)
button1.pack()

display_area = Label(window, text ="")
display_area.pack()

window.mainloop()


