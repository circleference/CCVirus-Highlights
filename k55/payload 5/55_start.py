from win32api import GetSystemMetrics
from playsound import playsound

import ctypes
from ctypes import wintypes 

import win32api, win32con, win32gui
import shake, pygame, os

pygame.init()
  
white = (255, 255, 255)
  
X = 500
Y = 500
  
display_surface = pygame.display.set_mode((X, Y), pygame.NOFRAME)
  
pygame.display.set_caption('troll')

image = pygame.image.load('55.png').convert_alpha()

hwnd = pygame.display.get_wm_info()['window']
    
user32 = ctypes.WinDLL("user32")
user32.SetWindowPos.restype = wintypes.HWND
user32.SetWindowPos.argtypes = [wintypes.HWND, wintypes.HWND, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.INT, wintypes.UINT]
user32.SetWindowPos(hwnd, -1, win32api.GetSystemMetrics(0) // 4, win32api.GetSystemMetrics(1) // 4, 0, 0, 0x0001)

fuchsia = (255, 0, 128)

win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE,
                       win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE) | win32con.WS_EX_LAYERED)

win32gui.SetLayeredWindowAttributes(hwnd, win32api.RGB(*fuchsia), 0, win32con.LWA_COLORKEY)

shake_ammount = 11

pygame.mixer.init()

os.chdir('..')
os.chdir('sounds')

pygame.mixer.music.load('Randomize163.wav')

os.chdir('..')
os.chdir('payload 4')

pygame.mixer.music.play()

while True :

    if shake_ammount != 5000:
        shake_ammount += 1
    if shake_ammount == 5000:
        pygame.quit()
        quit()

    shake_cords = shake.smoothshake((0, 0), shake_ammount)

    display_surface.fill(fuchsia)
    display_surface.blit(pygame.transform.scale(image, (X, Y)), shake_cords)
  
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
  
    pygame.display.update()
    pygame.display.flip()