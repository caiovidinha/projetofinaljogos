import pygame

class Boss(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()

        self.image = pygame.image.load("boss.png")

        self.rect = self.image.get_rect()

        self.rect.x = 100
        self.rect.y = 100

        self.attack_timer = pygame.time.get_ticks()

    def attack(self):
        pass

    def movement(self):
        pass

    def update(self):
        pass