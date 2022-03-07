import pygetwindow as gw
from win32api import GetSystemMetrics
import os, time

time.sleep(0.2)
win = gw.getWindowsWithTitle('AAAAAAAHHHHHHHH')[0]
x = int(GetSystemMetrics(0) / 2 - GetSystemMetrics(0))
y = int(GetSystemMetrics(1) / 2 - GetSystemMetrics(1))

def move():
    global x, y

    for s in range(520):
        time.sleep(0.01)
        win.move(3, 0)

    for s in range(520):
        time.sleep(0.01)
        win.move(-3, 0)

    move()

move()