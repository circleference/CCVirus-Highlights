import pygame, PIL

pygame.font.init()
pygame.font.get_init()

draw_bar = False
 
display_surface = pygame.display.set_mode((500, 500))
pygame.display.set_caption('I Dare You')
 
font1 = pygame.font.SysFont('freesanbold.ttf', 50)
font2 = pygame.font.SysFont('chalkduster.ttf', 40)
text1 = font1.render('Close Me', True, (0, 0, 0))
 
textRect1 = text1.get_rect()
textRect1.center = (250, 250)

bar = pygame.image.load('bar.png')

 
while True:
 
    display_surface.fill((255, 255, 255))
    display_surface.blit(text1, textRect1)
 
    for event in pygame.event.get():
 
        if event.type == pygame.QUIT:
            pygame.display.set_mode((500, 500), pygame.NOFRAME)
            draw_bar = True

    if draw_bar == True:
        text1 = font1.render(':) hehehe', True, (0, 0, 0))
 
    pygame.display.update()
    pygame.display.flip()