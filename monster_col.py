import pygame 

class Monster_col(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.image = pygame.image.load('assets/inimigos/monstercol.png')
        self.rect = self.image.get_rect(topleft = pos)
    
    def update(self,x_shift):
        self.rect.x += x_shift