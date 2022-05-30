from win32api import GetSystemMetrics
from playsound import playsound

import pyscreenshot as ImageGrab
import pygame, os, random, compress

import ctypes
from ctypes import wintypes 

import win32api
import win32con
import win32gui

def rand_win_pos():
    global win_x_pos, win_y_pos
    win_x_pos = str(random.randint(0, GetSystemMetrics(0)))
    win_y_pos = str(random.randint(0, GetSystemMetrics(1)))

rand_win_pos()

exec_string = str(win_x_pos + ',' + win_y_pos)


print(exec_string)

os.environ['SDL_VIDEO_WINDOW_POS'] = exec_string

os.chdir('..')
playsound('sounds\\Randomize91.wav')
os.chdir('payload 1')

def screenshot():
    im = ImageGrab.grab(backend="mss", childprocess=False)
    os.chdir('..')
    im.save('screen\\fullscreen_2.png')
    os.chdir('payload 2')

    play()

def play():
    os.chdir('..')
    playsound('sounds\\Randomize110.wav')
    os.chdir('payload 1')

screenshot()

pygame.init()
  
white = (255, 255, 255)
  
X = GetSystemMetrics(0) // 2
Y = GetSystemMetrics(1) // 2
  
display_surface = pygame.display.set_mode((X, Y), pygame.NOFRAME)
  
pygame.display.set_caption('lol')
os.chdir('..')
try:
    image = pygame.image.load('screen\\fullscreen_2.png').convert()
except:
    pygame.quit()
    quit()
os.chdir('payload 2')

hwnd = pygame.display.get_wm_info()['window']
    
user32 = ctypes.WinDLL("user32")
user32.SetWindowPos.restype = wintypes.HWND
user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.UINT]
user32.SetWindowPos(hwnd, -1, int(win_x_pos), int(win_y_pos), 0, 0, 0x0001)

fuchsia = (255, 0, 128)

win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)


while True :

    screenshot()
    rand_win_pos()

    user32.SetWindowPos(hwnd, -1, int(win_x_pos), int(win_y_pos), 0, 0, 0x0001)

    os.chdir('..')
    try:
        image = pygame.image.load('screen\\fullscreen_2.png').convert_alpha()
    except:
        pass
    os.chdir('payload 2')
    image = compress.sharp_compression(image, intensity=2).convert_alpha()

    rand_x = random.randint(0, X)
    rand_y = random.randint(0, Y)

    display_surface.fill(fuchsia)
    display_surface.blit(pygame.transform.scale(image, (X, Y)), (rand_x, rand_y))
  
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
  
    pygame.display.update()
    pygame.display.flip()