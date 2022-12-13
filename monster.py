import pygame
from support_enemies import importar_pasta

class Javali(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.vel_animacao = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.type = 'terrestre'
        self.name = 'javali'

        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2(0,0)
        self.direction.x = 1
        self.speed = 2
        self.life = 3
        self.hit = False
        self.hit_cooldown = 600
        self.hit_time = None

        self.status = 'idle'
        self.facing_right = True
    
    
    def get_status(self):
        if self.hit and self.life > 0:
            self.status = 'hit'
        elif self.hit and self.life == 0:
            self.status = 'dead'
        else:
            if self.direction.x != 0:
                self.status = 'run'
            else: 
                self.status = 'idle'
    
    def import_character_assets(self):
        character_path = 'assets/inimigos/javali/'
        self.animations = {'idle':[],'run':[],'hit':[],'dead':[]}

        for animation in self.animations.keys():
            caminho = character_path + animation
            self.animations[animation] = importar_pasta(caminho)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.vel_animacao
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]

        if not self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if self.hit:
            if current_time - self.hit_time >= self.hit_cooldown:
                self.hit = False
                if self.life == 0:
                    self.life = -1
                if self.life > 0:
                    if self.facing_right:
                        self.facing_right = False
                    else:
                        self.facing_right = True
                    


    def update(self,x_shift):
        self.rect.x += x_shift
        self.get_status()
        self.cooldown()
        self.animate()

class Abelha(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.vel_animacao = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.type = 'voador'
        self.name = 'abelha'

        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2(0,0)
        self.direction.y = 1
        self.speed = 2
        self.life = 2
        self.hit = False
        self.hit_cooldown = 600
        self.hit_time = None

        self.status = 'idle'
        self.facing_right = False
    
    
    def get_status(self):
        if self.hit and self.life > 0:
            self.status = 'hit'
        elif self.hit and self.life == 0:
            self.status = 'dead'
        else:
            self.status = 'idle'
    
    def import_character_assets(self):
        character_path = 'assets/inimigos/abelha/'
        self.animations = {'idle':[],'hit':[],'dead':[]}

        for animation in self.animations.keys():
            caminho = character_path + animation
            self.animations[animation] = importar_pasta(caminho)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.vel_animacao
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]

        if not self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if self.hit:
            if current_time - self.hit_time >= self.hit_cooldown:
                self.hit = False
                if self.life == 0:
                    self.life = -1
                
    def update(self,x_shift):
        self.rect.x += x_shift
        self.get_status()
        self.cooldown()
        self.animate()

class Caramujo(pygame.sprite.Sprite):
    def __init__(self,pos):
        super().__init__()
        self.import_character_assets()
        self.frame_index = 0
        self.vel_animacao = 0.15
        self.image = self.animations['slide'][self.frame_index]
        self.type = 'terrestre'
        self.name = 'caramujo'

        self.hidden = False
        self.unhiding = False
        self.hide_cd = 800
        self.hide_time = None

        self.rect = self.image.get_rect(topleft = pos)

        self.direction = pygame.math.Vector2(0,0)
        self.direction.x = 1
        self.speed = 1
        self.life = 1
        self.hit = False
        self.hit_cooldown = 1200
        self.hit_time = None

        self.status = 'slide'
        self.facing_right = True
     
    def get_status(self):
        if not self.hidden and not self.unhiding:
            if self.hit and self.life == 0:
                self.status = 'dead'
                self.speed = 0
            else:
                if self.direction.x != 0:
                    self.status = 'slide'
                    self.speed = 1
        else:
            self.speed = 0
            if self.hidden:
                self.status = 'hidden'
            elif self.unhiding:
                self.status = 'unhide'
    
    def import_character_assets(self):
        character_path = 'assets/inimigos/caramujo/'
        self.animations = {'slide':[],'hidden':[],'unhide':[],'dead':[]}

        for animation in self.animations.keys():
            caminho = character_path + animation
            self.animations[animation] = importar_pasta(caminho)

    def animate(self):
        animation = self.animations[self.status]

        self.frame_index += self.vel_animacao
        if self.frame_index >= len(animation):
            if self.status == 'dead':
                self.frame_index = len(animation)-1
            elif self.status == 'slide':
                self.frame_index = 0
            elif self.status == 'unhide':
                self.frame_index = len(animation)-1
            elif self.status == 'hidden':
                self.frame_index = 0 

        image = animation[int(self.frame_index)]

        if not self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

    def cooldown(self):
        current_time = pygame.time.get_ticks()
        if self.hit:
            if current_time - self.hit_time >= self.hit_cooldown:
                self.hit = False
                if self.life == 0:
                    self.life = -1
                if self.life > 0:
                    if self.facing_right:
                        self.facing_right = False
                    else:
                        self.facing_right = True
        #TODO
        if self.unhiding:
            if current_time - self.hide_cd >= self.hide_time:
                    self.unhiding = False
                    self.hidden = False
                    self.status = 'slide'
                    
    def update(self,x_shift):
        self.rect.x += x_shift
        self.get_status()
        self.cooldown()
        self.animate()
        
        