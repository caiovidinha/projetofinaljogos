import pygame 

class Collectable(pygame.sprite.Sprite):
    def __init__(self,pos,name):
        super().__init__()
        caminho = 'assets/collects/' + name
        self.image = pygame.image.load(caminho)
        self.rect = self.image.get_rect(topleft = pos)
        self.name = name
    def update(self,x_shift):
        self.rect.x += x_shift