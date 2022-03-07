import os
import pygame
import ctypes
user32 = ctypes.windll.user32
window_xy = user32.GetSystemMetrics(0) - user32.GetSystemMetrics(0) / 1, user32.GetSystemMetrics(1) - user32.GetSystemMetrics(1) / 18

os.environ['SDL_VIDEO_WINDOW_POS'] = "%d,%d" % window_xy

pygame.init()
screen = pygame.display.set_mode((500,55), pygame.NOFRAME)
pygame.display.set_caption('warning')

font1 = pygame.font.SysFont('freesanbold.ttf', 30)
text1 = font1.render('your files are not actually being deleted', True, (0, 0, 0))

textRect1 = text1.get_rect()
textRect1.center = (250, 30)

running = True

SetWindowPos = ctypes.windll.user32.SetWindowPos

NOSIZE = 1
NOMOVE = 2
TOPMOST = -1
NOT_TOPMOST = -2

def alwaysOnTop(yesOrNo):
    zorder = (NOT_TOPMOST, TOPMOST)[yesOrNo]
    hwnd = pygame.display.get_wm_info()['window']
    SetWindowPos(hwnd, zorder, 0, 0, 0, 0, NOMOVE|NOSIZE)


while running:
    pygame.event.get()

    alwaysOnTop(True)

    screen.fill((255, 255, 255))
    screen.blit(text1, textRect1)

    pygame.display.flip()
    