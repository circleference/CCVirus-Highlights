from win32api import GetSystemMetrics
from playsound import playsound
from tkinter import *

import random, time, os

def HighlightSection(Rect=(100,100,300,200), Color = 'red', Duration = 3):
    win= Tk()
    GeometryString = str(Rect[0])+'x'+str(Rect[1])+'+' \
                     +str(Rect[2])+'+'+str(Rect[3])
    win.geometry(GeometryString) # "200x100+300+250" # breite, höhe, x, y # 
    win.configure(background=Color)
    win.overrideredirect(1)
    win.attributes('-alpha', 0.3)
    win.wm_attributes('-topmost', 1)
    win.after(Duration * 10, lambda: win.destroy())
    win.mainloop()

colors = ['green', 'blue', 'red', 'yellow', 'pink', 'orange', 'white', 'black']

dur = 100

while True:
    HighlightSection(Rect=(random.randint(100, 1400),random.randint(100, 1400),random.randint(100, GetSystemMetrics(0)),random.randint(100, GetSystemMetrics(1))), Color = colors[random.randint(0, len(colors) - 1)], Duration = dur)

    os.chdir('..')
    os.chdir('sounds')

    rand_s = random.randint(0, 2)

    print(rand_s)

    if dur != 20:
        dur -= 10

    if rand_s == 0:

        playsound('Randomize122.wav')

    elif rand_s == 1:

        playsound('Randomize114.wav')

    elif rand_s == 2:

        playsound('Randomize116.wav')

    os.chdir('..')

    os.chdir('payload 3')