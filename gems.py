import pygame
from support import importar_pasta

class Gem(pygame.sprite.Sprite):
    def __init__(self,pos,color):
        super().__init__()
        self.import_assets()
        self.frame_index = 0
        self.vel_animacao = 0.15
        self.image = self.animations[color][self.frame_index]
        self.color = color

        self.rect = self.image.get_rect(topleft = pos)

    
    def import_assets(self):
        character_path = 'assets/gems/'
        self.animations = {'blue':[],'red':[]}

        for animation in self.animations.keys():
            caminho = character_path + animation
            self.animations[animation] = importar_pasta(caminho)

    def animate(self):
        animation = self.animations[self.color]

        self.frame_index += self.vel_animacao
        if self.frame_index >= len(animation):
                self.frame_index = 0

        self.image = animation[int(self.frame_index)]

    def update(self,x_shift):
        self.rect.x += x_shift
        self.animate()