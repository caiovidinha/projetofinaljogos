import pygame, sys
from settings import * 
from level import Level


# Pygame setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
pygame.display.set_caption('Fire Soul')
bg = pygame.image.load("assets/bg.png")
clock = pygame.time.Clock()
level = Level(level0_map,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    
    screen.blit(bg,(0,0))
    level.run()
    
    pygame.display.update()
    clock.tick(60)