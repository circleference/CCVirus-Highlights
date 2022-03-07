import pygame
import ctypes
user32 = ctypes.windll.user32
screensize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)

pygame.init()
  
display_surface = pygame.display.set_mode(screensize, pygame.FULLSCREEN)
pygame.display.set_caption('Craig')
  
while True :
    display_surface.fill((0, 0, 0))
  
    for event in pygame.event.get() :
        if event.type == pygame.QUIT :
            pygame.quit()
            quit()
        
        pygame.display.update() 
             