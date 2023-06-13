from tkinter import Tk

from tkinter import *
import random

window = Tk()
window.geometry('600x600')

class Fire:
    image = PhotoImage(file='elements/free-icon-fire-9509865.png').subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Ground):
            return Clay

class Water:
    image = PhotoImage(file='elements/free-icon-water-drop-4246703.png').subsample(4, 4)

class Ground:
    image = PhotoImage(file='elements/ground.png').subsample(4, 4)
    def __add__(self, other):
        if isinstance(other, Fire):
            return Clay

class Wind:
    image = PhotoImage(file='elements/wind.png').subsample(4, 4)

class Clay:
    image = PhotoImage(file='elements/free-icon-pottery-7942410.png').subsample(4, 4)



canvas = Canvas(window, width=600, height=600)
canvas.pack()

elements = [Fire(), Ground(), Water(), Wind()]

for elem in elements:
    img = canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=elem.image)

def move(event):
    images_id = canvas.find_overlapping(event.x, event.y, event.x+10, event.y+10)
    canvas.coords(images_id, event.x, event.y)
    if len(images_id) == 2:
        element1 = elements[images_id[0]-1]
        element2 = elements[images_id[1]-1]
        new_element = element1+element2
        if new_element not in elements:
            canvas.create_image(random.randint(50, 550), random.randint(50, 550), image=new_element.image)
            elements.append(new_element)

window.bind('<B1-Motion>', move)

window.mainloop()


