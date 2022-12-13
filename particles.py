from support import importar_pasta
import pygame

class ParticleEffect(pygame.sprite.Sprite):
    def __init__(self,pos,type):
        super().__init__()
        self.frame_index = 0
        self.vel_animacao = 0.45
        if type == 'jump':
            self.frames = importar_pasta('assets/player/dust_particles/jump')
        if type == 'land':
            self.frames = importar_pasta('assets/player/dust_particles/land')

        self.image = self.frames[self.frame_index]
        self.rect = self.image.get_rect(center = pos)

    def animate(self):
        self.frame_index += self.vel_animacao
        if self.frame_index >= len(self.frames):
            self.kill()
        else:
            self.image = self.frames[int(self.frame_index)]
            

    def update(self,x_shift):
        self.animate()
        self.rect.x += x_shift