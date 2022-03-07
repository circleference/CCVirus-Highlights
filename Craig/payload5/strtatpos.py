import pygetwindow as gw
from win32api import GetSystemMetrics
import os, time

os.system('start craig.bat')

time.sleep(0.2)
win = gw.getWindowsWithTitle('NO CRAIG NO !!!!!!!!!!!!!!!!!!!!!')[0]
x = int(GetSystemMetrics(0) / 2 - GetSystemMetrics(0))
y = int(GetSystemMetrics(1) / 2 - GetSystemMetrics(1))

def move():
    global x, y

    win.move(800, 100)

move()