import pygame
from support import importar_pasta

class Fireball(pygame.sprite.Sprite):
    def __init__(self,pos,right,speed,range):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.vel_animacao = 0.3
        self.image = self.animations['fireball'][self.frame_index]
        self.right = right
        self.speed = speed
        self.range = range
        self.pos = pos
        self.rect = self.image.get_rect(midleft = pos)
        self.status = 'fireball'
        
    def import_character_assets(self):
        character_path = 'assets/player/fireball/'
        self.animations = {'fireball':[],'hit':[]}

        for animation in self.animations.keys():
            caminho = character_path + animation
            self.animations[animation] = importar_pasta(caminho)
    
    def animate(self):
        animation = self.animations[self.status]
        self.frame_index += self.vel_animacao
        if self.frame_index >= len(animation):
            self.frame_index = 0
        
        image = animation[int(self.frame_index)]
        if self.right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image
    
    def update(self,x_shift):
        self.rect.x += x_shift + self.speed
        self.animate()
        
    
