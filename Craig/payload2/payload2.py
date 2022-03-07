import os, time

os.chdir('sounds')
os.system('start /min boom.vbs')
os.chdir('..')

os.environ['SDL_VIDEO_WINDOW_POS'] = "0,-20"

import pygame

pygame.init()
screen = pygame.display.set_mode((150,150), pygame.NOFRAME)
pygame.display.set_caption('AAAAAAAHHHHHHHH')

frame = 1
thread = 1
running = True
files_in_dir = os.listdir('assets/frames/')

os.system('start /min move.py')

print(type(files_in_dir))

while running:
    pygame.event.get()
    if frame != 105:
        frame += 1
    else:
        frame = 1

    dwayne_frame = pygame.image.load(os.path.join(f'assets/frames/{str(frame)}.png'))
    dwayne_frame = pygame.transform.scale(dwayne_frame, (150, 150))

    screen.fill((0, 0, 0))
    screen.blit(dwayne_frame, (1, 1))
    pygame.display.flip()
    