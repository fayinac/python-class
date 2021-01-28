from tkinter import *

window = Tk()
window.title('Song Lyric Generator')

window.configure(bg = 'MediumPurple1')

top_label = Label(window, text = '', bg = "MediumPurple1")
top_label.pack()

red_label = Label(window, text = 'Enter something red e.g. roses:', bg = "MediumPurple1", fg = 'black')
red_label.pack()

red = Entry(window, text='')
red.pack()

top_label = Label(window, text = '', bg = "MediumPurple1")
top_label.pack()

blue_label = Label(window, text = 'Enter something blue e.g. violets', bg = "MediumPurple1", fg = 'black')
blue_label.pack()

blue = Entry(window, text='')
blue.pack()

top_label = Label(window, text = '', bg = "MediumPurple1")
top_label.pack()

like_label = Label(window, text = 'Something you love, e.g. puppies', bg = "MediumPurple1", fg = 'black')
like_label.pack()

like = Entry(window, text='')
like.pack()

top_label = Label(window, text = '', bg = "MediumPurple1")
top_label.pack()

verb_label = Label(window, text = 'Verb, e.g. singing', bg = "MediumPurple1", fg = 'black')
verb_label.pack()

verb = Entry(window, text='')
verb.pack()

top_label = Label(window, text = '', bg = "MediumPurple1")
top_label.pack()

def create_song():
   poem_string = red.get() + '''are red\n''' + blue.get() + '''are blue\n''' + 'i like' + like.get() + '\nbut not as much as I love' + verb.get() + 'with you!'
   poem_display.configure(text = poem_string)

button = Button(window, text = 'Create Song', compound = TOP, command = create_song)
button.pack()

poem_display = Label(window, text = "")
poem_display.pack

window.mainloop()
