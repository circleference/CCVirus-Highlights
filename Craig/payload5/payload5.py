import os, time

os.chdir('sounds')
os.system('taskkill /f /im explorer.exe')
os.system('start /min boom.vbs')
os.chdir('..')

os.system('start strtatpos.py')
os.system('start warning.py')

os.environ['SDL_VIDEO_WINDOW_POS'] = "200,100"

import pygame

pygame.init()
screen = pygame.display.set_mode((500,700), pygame.NOFRAME)
pygame.display.set_caption('NO CRAIG NO!!!!!!!!!!')

frame = 1
thread = 1
running = True
files_in_dir = os.listdir('assets/frames/')

print(type(files_in_dir))

while running:
    pygame.event.get()
    if frame != 2:
        frame += 1
    else:
        frame = 1

    craig = pygame.image.load(os.path.join(f'assets/frames/{str(frame)}.png'))
    craig = pygame.transform.scale(craig, (500, 700))

    screen.fill((0, 0, 0))
    screen.blit(craig, (0, 0))
    time.sleep(1)
    pygame.display.flip()
    