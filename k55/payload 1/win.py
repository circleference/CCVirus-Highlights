from win32api import GetSystemMetrics
from playsound import playsound

import pyscreenshot as ImageGrab
import pygame, os, random

import ctypes
from ctypes import wintypes 


win_x_pos = str(random.randint(0, GetSystemMetrics(0)))
win_y_pos = str(random.randint(0, GetSystemMetrics(1)))

exec_string = str(win_x_pos + ',' + win_y_pos)


print(exec_string)

os.environ['SDL_VIDEO_WINDOW_POS'] = exec_string

os.chdir('..')


def screenshot():
    im = ImageGrab.grab(backend="mss", childprocess=False)
    im.save('screen\\fullscreen.png')

    play()

def play():
    playsound('sounds\\Randomize90.wav')

screenshot()

pygame.init()
  
white = (255, 255, 255)
  
X = GetSystemMetrics(0) // 3
Y = GetSystemMetrics(1) // 3
  
display_surface = pygame.display.set_mode((X, Y), pygame.NOFRAME)
  
pygame.display.set_caption('lol')
image = pygame.image.load('screen\\fullscreen.png').convert()

hwnd = pygame.display.get_wm_info()['window']
    
user32 = ctypes.WinDLL("user32")
user32.SetWindowPos.restype = wintypes.HWND
user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.UINT]
user32.SetWindowPos(hwnd, -1, 600, 300, 0, 0, 0x0001)

while True :

    screenshot()

    image = pygame.image.load('screen\\fullscreen.png').convert()
  
    display_surface.fill(white)
    display_surface.blit(pygame.transform.scale(image, (X, Y)), (0, 0))
  
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
  
    pygame.display.update()
    pygame.display.flip()