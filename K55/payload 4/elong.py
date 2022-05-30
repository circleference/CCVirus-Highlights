
from win32api import GetSystemMetrics

from pygame.locals import *
import pygame, random, os

win_x_pos = str(random.randint(0, GetSystemMetrics(0)))
win_y_pos = str(random.randint(0, GetSystemMetrics(1)))

exec_string = str(win_x_pos + ',' + win_y_pos)


print(exec_string)

os.environ['SDL_VIDEO_WINDOW_POS'] = exec_string

pygame.init()

X = 132
Y = 152

screen = pygame.display.set_mode((X, Y), pygame.NOFRAME)

L = pygame.image.load('L.jpg').convert()
L = pygame.transform.scale(L, (X, Y))

clock = pygame.time.Clock()

pygame.mixer.init()

os.chdir('..')
os.chdir('sounds')

pygame.mixer.music.load("Randomize135.wav")

os.chdir('..')
os.chdir('payload 4')

while True:

    screen.fill((255, 255, 255))

    X += 1

    L = pygame.transform.scale(L, (X, Y))
    screen = pygame.display.set_mode((X, Y), pygame.NOFRAME)

    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
    
    pygame.mixer.music.play()

    screen.blit(L, (0, 0))

    clock.tick(150)

    pygame.display.update()
    pygame.display.flip()
