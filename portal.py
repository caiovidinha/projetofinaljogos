import pygame
from support_portal import importar_pasta

class Portal(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.vel_animacao = 0.25
        self.image = self.animations['portal'][self.frame_index]

        self.rect = self.image.get_rect(topleft = pos)
          

    def import_character_assets(self):
        character_path = 'assets/'
        self.animations = {'portal':[]}

        for animation in self.animations.keys():
            caminho = character_path + animation
            self.animations[animation] = importar_pasta(caminho)
    
    def animate(self):
        animation = self.animations['portal']

        self.frame_index += self.vel_animacao

        if self.frame_index >= len(animation):
            self.frame_index = 0

        self.image = animation[int(self.frame_index)]
        

    def update(self,x_shift):
        self.rect.x += x_shift
        self.animate()