import pygame
from support_player import importar_pasta
from math import sin

class Player(pygame.sprite.Sprite):
    def __init__(self,pos,surface,create_jump_particles,gems,blue_gems,max_health,current_health,max_stamina,regen_rate,current_stamina,blue_level,red_level,bgems,rgems,damage,speed,current_level,collects,main_menu):
        super().__init__()
        self.import_character_assets()
        self.import_run_dust()

        #Lógica de animação
        self.frame_index = 0
        self.vel_animacao = 0.15
        self.image = self.animations['idle'][self.frame_index]
        
        #Armazenar quais itens foram coletados pelo jogador
        self.collectables = collects

        self.fade = False
        
        
        #Atributos do jogador
        self.max_health = max_health
        self.current_health = current_health
        self.max_stamina = max_stamina
        self.stamina_regen_rate = regen_rate
        self.current_stamina = current_stamina
        self.gems = gems
        self.blue_gems = blue_gems
        self.blue_level = blue_level
        self.red_level = red_level
        self.attack_damage = damage
        self.bgems = bgems
        self.rgems = rgems

        #Para medir a passagem de fases
        self.level = current_level


        #Definir se a animação será do primeiro ou segundo ataque
        self.attack1 = 1

        #Correção de bug que joga o player para cima dos blocos ao atacar
        self.rect = self.image.get_rect(topleft = pos)
        self.facing_right = True
        self.on_ground = True
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
        self.fire_attack = False

        #Lógica de animação de partículas de poeira
        self.dust_frame_index = 0
        self.dust_speed = 0.15
        self.display_surface = surface
        self.create_jump_particles = create_jump_particles

        #Movimentação x e y do player
        self.direction = pygame.math.Vector2(0,0)
        self.speed = speed
        self.cur_speed = speed
        self.gravity = 0.8
        self.jump_speed = -16

        #Tempo da "animação" de game over    
        self.game_over = 100

        #Sons
        self.dodge_sound = pygame.mixer.Sound('assets/sounds/88_Teleport_02.wav')
        self.attack_sound = pygame.mixer.Sound('assets/sounds/56_Attack_03.wav')
        self.step_sound = pygame.mixer.Sound('assets/sounds/08_Step_rock_02.wav')

        #Cooldowns
        self.dodge = False
        self.dodge_time = None
        self.dodge_duration = 1000

        self.invincible = False
        self.invincibilty_duration = 800
        self.hurt_time = 0
        
        self.level_up = False
        self.level_up_duration = 1200
        self.level_up_time = 0

        self.attacking = False
        self.attack_cooldown = 400
        self.attack_time = None

        #status
        self.status = 'idle'
        self.opac = 255
        self.last_level = None
 
    def get_status(self):
        #Define o status do player, dodge em primeiro lugar pois todas as ações são bloqueadas ao desviar
        if not self.dodge:
            #Após isso, verificamos se o player está morto ou entrando em um portal, para impedir também de realizar ações e animações
            if self.status != 'portal' and self.status != 'dead':
                if self.direction.y < 0 and not self.attacking:
                    self.status = 'jump'
                elif self.direction.y > 1 and not self.attacking:
                    self.status = 'fall'
                else:
                    if self.direction.x != 0 and not self.attacking and not self.fire_attack:
                        self.status = 'run'
                    elif not self.attacking and not self.fire_attack:
                        self.status = 'idle'
            
                if self.attacking:
                    if self.on_ground:
                        self.direction.x = 0

                    if self.attack1 == -1:
                        self.status = 'attack'
                    else:
                        self.status = 'attack_2' 

                if self.fire_attack:
                    if self.on_ground:
                        self.direction.x = 0
                    self.status = 'fire_attack'
        else:
            self.status = 'dodge'
            
    def stamina_regen(self):
        #Define a regeneração de stamina
        if self.current_stamina < self.max_stamina:
            self.current_stamina += self.stamina_regen_rate

    def import_character_assets(self):
        #Importa as animações das pastas determinadas pelo "status" do player
        character_path = 'assets/player/'
        self.animations = {'idle':[],'run':[],'jump':[],'fall':[],'attack':[],'attack_2':[],'fire_attack':[], 'portal':[],'dead':[],'dodge':[]}

        for animation in self.animations.keys():
            caminho = character_path + animation
            self.animations[animation] = importar_pasta(caminho)
    
    def import_run_dust(self):
        #Importa as animações de partículas
        self.run_dust = importar_pasta('assets/player/dust_particles/run')

    def animate(self):
        #Basicamente incrementa o index do frame pela velocidade de animação, fazendo as imagens percorrerem a lista armazenada pela função acima
        animation = self.animations[self.status]

        self.frame_index += self.vel_animacao
        #Nessa sequência de "ifs" é definido onde cada animação para ou retorna ao index inicial(loop)
        if self.frame_index >= len(animation):
            if self.status == 'idle' or self.status == 'run':
                self.frame_index = 0
            elif self.status == 'jump' or self.status == 'fall' or self.status == 'dead':
                self.frame_index = len(animation)-1
            if self.status == 'attack':
                self.frame_index = 0
            elif self.status == 'attack_2':
                self.frame_index = 0
            elif self.status == 'fire_attack':
                self.frame_index = 0
            elif self.status == 'dodge':
                self.frame_index = 0
            if self.status == 'portal':
                self.frame_index = len(animation)-1
                self.image.set_alpha(self.opac)
                if self.opac > 0:
                    self.rect.x += 10
                else:
                    self.level += 1

        
        image = animation[int(self.frame_index)]

        #Inverte a animação
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image
        
        #Animação de invincibilidade
        if self.invincible and self.status != 'dead':
            alpha = self.invisible_wave()
            self.image.set_alpha(alpha)
        elif not self.invincible and self.status != 'portal':
            self.image.set_alpha(255)


        #Correção dos bugs de teletransporte do player (no chão)
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ground and self.attacking and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.attacking and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        
        #Correção dos bugs de teletransporte do player (no teto)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)

    def invisible_wave(self):
        #A função seno retorna valores entre -1 e 1, apenas defini para que, quando negativos, o player tenha opacidade zerada
        value = sin(pygame.time.get_ticks())
        if value >= 0: return 255
        else: return 0

    def player_dodge(self):
        #Função que aplica o "poder" de dodge do player, define gasto mínimo e movimentação
        if not self.dodge and self.current_stamina > 70:
            self.dodge_sound.play()
            self.dodge = True
            self.dodge_time = pygame.time.get_ticks()
            if self.facing_right:
                self.direction.x = 10
            else:
                self.direction.x = -10
            self.current_stamina -= 70

    def run_dust_animation(self):
        #Animação das partículas de poeira ao correr
        if self.status == 'run' and self.on_ground:
            self.dust_frame_index += self.dust_speed
            if self.dust_frame_index >= len(self.run_dust):
                self.dust_frame_index = 0

            dust_particle = self.run_dust[int(self.dust_frame_index)]

            if self.facing_right:
                pos = self.rect.bottomleft - pygame.math.Vector2(10,10)
                self.display_surface.blit(dust_particle,pos)
            else:
                pos = self.rect.bottomright - pygame.math.Vector2(0,10)
                flipped_dust_particle = pygame.transform.flip(dust_particle,True,False)
                self.display_surface.blit(flipped_dust_particle,pos)

    def get_input(self):
        #Inputs do teclado
        keys = pygame.key.get_pressed()
        if not self.attacking:
            if keys[pygame.K_RIGHT] and not self.dodge:
                self.direction.x = 1
                self.facing_right = True
            elif keys[pygame.K_LEFT] and not self.dodge:
                self.direction.x = -1
                self.facing_right = False
            else:
                self.direction.x = 0
            
            if keys[pygame.K_c] and self.blue_level >= 2:
                self.player_dodge()


            if keys[pygame.K_SPACE] and self.on_ground:
                self.jump()
                self.create_jump_particles(self.rect.midbottom)
            
            if keys[pygame.K_z] and not self.attacking:
                if self.current_stamina > 30:
                    self.attack_sound.play()
                    self.attacking = True
                    self.attack_time = pygame.time.get_ticks()
                    self.current_stamina -= 25
            if keys[pygame.K_x] and not self.fire_attack and self.red_level >= 2:
                if self.current_stamina > 30:
                    self.fire_attack = True
                    self.attack_time = pygame.time.get_ticks()
                    self.current_stamina -= 60
            
            if keys[pygame.K_RETURN]:
                self.main_menu = False
                
    def cooldowns(self):
        #Função que aplica os cooldowns com um "relógio feito com a função get_ticks()"
        current_time = pygame.time.get_ticks()
        
        if self.attacking:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.attacking = False
                self.attack1 *= -1

        if self.fire_attack:
            if current_time - self.attack_time >= self.attack_cooldown:
                self.fire_attack = False
                
        if self.invincible:
            if current_time - self.invincibilty_duration >= self.hurt_time:
                self.invincible = False

        if self.level_up:
            if current_time - self.level_up_time >= self.level_up_duration:
                self.level_up = False
        
        if self.dodge:
            if current_time - self.dodge_time >= self.dodge_duration:
                self.dodge = False

    def apply_gravity(self):
        #Simplesmente aplica a gravidade
        self.direction.y += self.gravity
        self.rect.y += self.direction.y

    def jump(self):
        #Simplesmente faz o player "pular"
        self.direction.y = self.jump_speed

    def update(self):
        #Atualização constante e invocação das funções
        self.get_input()
        self.cooldowns()
        self.stamina_regen()
        self.get_status()
        self.run_dust_animation()
        self.animate()
        