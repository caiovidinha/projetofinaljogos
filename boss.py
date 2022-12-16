import pygame
from support_player import importar_pasta
from math import sin

class Boss(pygame.sprite.Sprite):
    def __init__(self,pos,collects):
        super().__init__()
        self.import_character_assets()

        self.frame_index = 0
        self.vel_animacao = 0.2
        self.image = self.animations['idle'][self.frame_index]
        self.status = 'idle'
        self.invincible = False
        self.attacking = False
        self.attackcooldown = False

        self.rect = self.image.get_rect(center = pos)
        self.facing_right = False

        if collects != []:
            for collectable in collects:
                if collectable == 'fang':
                    self.damage = 10
                else:
                    self.damage = 30

                if collectable == 'eye':
                    self.speed = 2
                else:
                    self.speed = 4

                if collectable == 'fur':
                    self.attack_cooldown = 3000
                else:
                    self.attack_cooldown = 2000

                if collectable == 'scalp':
                    self.fire_resistant = False
                else:
                    self.fire_resistant = True

                if collectable == 'blood':
                    self.hp = 150
                else:
                    self.hp = 300
        else:
            self.damage = 30
            self.speed = 4
            self.attack_cooldown = 3000
            self.fire_resistant = True
            self.hp = 300

        self.current_hp = self.hp
    
    def import_character_assets(self):
        #Importa as animações das pastas determinadas pelo "status" do player
        character_path = 'assets/boss/'
        self.animations = {'idle':[],'attack':[]}

        for animation in self.animations.keys():
            caminho = character_path + animation
            self.animations[animation] = importar_pasta(caminho)

    def animate(self):
    #Basicamente incrementa o index do frame pela velocidade de animação, fazendo as imagens percorrerem a lista armazenada pela função acima
        animation = self.animations[self.status]

        self.frame_index += self.vel_animacao
        #Nessa sequência de "ifs" é definido onde cada animação para ou retorna ao index inicial(loop)
        if self.frame_index >= len(animation):
            if self.status == 'idle':
                self.frame_index = 0
            elif self.status == 'attack':
                 self.frame_index = 0
                 
               

        image = animation[int(self.frame_index)]

        #Inverte a animação
        if not self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image
        
        #Animação de invincibilidade
        if self.invincible:
            alpha = self.invisible_wave()
            self.image.set_alpha(alpha)
        else:
            self.image.set_alpha(255)

    def invisible_wave(self):
        #A função seno retorna valores entre -1 e 1, apenas defini para que, quando negativos, o player tenha opacidade zerada
        value = sin(pygame.time.get_ticks())
        if value >= 0: return 255
        else: return 0

    def get_status(self):
        if self.attacking:
            self.status = 'attack'
        else:
            self.status = 'idle'

    def attack(self):
        self.attacking = True
        

    def cooldowns(self):
        if self.attacking:
            if pygame.time.get_ticks() - self.attack_time >= 1000:
                self.attacking = False
        if self.attackcooldown:
            if pygame.time.get_ticks() - self.attack_time >= self.attack_cooldown:
                self.attackcooldown = False
        if self.invincible:
            if pygame.time.get_ticks() - self.damage_time >= 1000:
                self.invincible = False

                

    def movement(self):
        pass

    def update(self,x_shift):
        self.animate()
        self.cooldowns()
        self.get_status()
        self.rect.x += x_shift
