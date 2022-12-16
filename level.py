import pygame
from tiles import Tile
from settings import *
from player import Player
from monster import Javali,Abelha,Caramujo
from monster_col import Monster_col
from fireball import Fireball
from portal import Portal
from gems import Gem
from particles import ParticleEffect
from ui import UI
from menu import Menu
from collectables import Collectable
from cutscenes import Cutscene
from boss import Boss

class Level:
    def __init__(self,level_data,surface):
        self.display_surface = surface
       
        self.setup_level(level_data,0,20,100,100,100,0.5,100,0,0,0,0,10,8,0,[],True)
        self.game_state = 'INGAME'
        self.dialogue_text = 0

        self.world_shift = 0
        self.current_x = 0
        self.current_level = 0

        #audio
        self.gem_sound = pygame.mixer.Sound('assets/sounds/013_Confirm_03.wav')
        self.jump_sound = pygame.mixer.Sound('assets/sounds/30_Jump_03.wav')
        self.hit_sound = pygame.mixer.Sound('assets/sounds/61_Hit_03.wav')
        self.menu_sound = pygame.mixer.Sound('assets/sounds/001_Hover_01.wav')
        self.fireball_sound = pygame.mixer.Sound('assets/sounds/04_Fire_explosion_04_medium.wav')
        self.boss_attack_sound = pygame.mixer.Sound('assets/sounds/55_Encounter_02.wav')
        self.land_sound = pygame.mixer.Sound('assets/sounds/45_Landing_01.wav')
        self.menu_music = pygame.mixer.Sound('assets/sounds/music/xDeviruchi - Decisive Battle.wav')
        self.game_music = pygame.mixer.Sound('assets/sounds/music/xDeviruchi - The Icy Cave .wav')
        self.game_music.play(loops=-1)


        self.fireball = pygame.sprite.Group()

        self.hud = UI(self.display_surface)
        self.menu = Menu(self.display_surface)
        self.cutscene = Cutscene(self.display_surface)

        self.player_on_ground = False

        self.gems = 0

        self.dust_sprite = pygame.sprite.GroupSingle()

    def create_jump_particles(self,pos):
        if self.player.sprite.status != 'portal':
            if self.player.sprite.facing_right:
                pos -= pygame.math.Vector2(2,10)
            else:
                pos += pygame.math.Vector2(2,-10)
            jump_particle = ParticleEffect(pos, 'jump')
            self.dust_sprite.add(jump_particle)
            self.jump_sound.play()

    def create_landing_dust(self):
        if not self.player_on_ground and self.player.sprite.on_ground and not self.dust_sprite.sprites():
            if self.player.sprite.facing_right:
                offset = pygame.math.Vector2(10,15)
            else:
                offset = pygame.math.Vector2(-10,15)
            fall_dust_particle = ParticleEffect(self.player.sprite.rect.midbottom-offset,'land')
            self.dust_sprite.add(fall_dust_particle)
            self.jump_sound.play()

    def setup_level(self,layout,gems,blue_gems,max_health,current_health,max_stamina,regen_rate,current_stamina,blue_level,red_level,bgems,rgems,damage,speed,current_level,collects,main_menu):
        self.tiles = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.boss = pygame.sprite.GroupSingle()
        self.monster = pygame.sprite.Group()
        self.monster_col = pygame.sprite.Group()
        self.fly_col = pygame.sprite.Group()
        self.portal = pygame.sprite.GroupSingle()
        self.bgems = pygame.sprite.Group()
        self.collectables = pygame.sprite.Group()

        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == 'Q':
                    tile = Tile((x,y),'assets/tiles/grass/topleft.png')
                    self.tiles.add(tile)
                if cell == 'W':
                    tile = Tile((x,y),'assets/tiles/grass/midtop.png')
                    self.tiles.add(tile)
                if cell == 'E':
                    tile = Tile((x,y),'assets/tiles/grass/topright.png')
                    self.tiles.add(tile)
                if cell == 'A':
                    tile = Tile((x,y),'assets/tiles/grass/midleft.png')
                    self.tiles.add(tile)
                if cell == 'S':
                    tile = Tile((x,y),'assets/tiles/grass/center.png')
                    self.tiles.add(tile)
                if cell == 'D':
                    tile = Tile((x,y),'assets/tiles/grass/midright.png')
                    self.tiles.add(tile)
                if cell == 'Z':
                    tile = Tile((x,y),'assets/tiles/grass/bottomleft.png')
                    self.tiles.add(tile)
                if cell == 'X':
                    tile = Tile((x,y),'assets/tiles/grass/midbottom.png')
                    self.tiles.add(tile)
                if cell == 'C':
                    tile = Tile((x,y),'assets/tiles/grass/bottomright.png')
                    self.tiles.add(tile)

                if cell == 'R':
                    tile = Tile((x,y),'assets/tiles/rock/topleft.png')
                    self.tiles.add(tile)
                if cell == 'T':
                    tile = Tile((x,y),'assets/tiles/rock/midtop.png')
                    self.tiles.add(tile)
                if cell == 'Y':
                    tile = Tile((x,y),'assets/tiles/rock/topright.png')
                    self.tiles.add(tile)
                if cell == 'F':
                    tile = Tile((x,y),'assets/tiles/rock/midleft.png')
                    self.tiles.add(tile)
                if cell == 'G':
                    tile = Tile((x,y),'assets/tiles/rock/center.png')
                    self.tiles.add(tile)
                if cell == 'H':
                    tile = Tile((x,y),'assets/tiles/rock/midright.png')
                    self.tiles.add(tile)
                if cell == 'V':
                    tile = Tile((x,y),'assets/tiles/rock/bottomleft.png')
                    self.tiles.add(tile)
                if cell == 'B':
                    tile = Tile((x,y),'assets/tiles/rock/midbottom.png')
                    self.tiles.add(tile)
                if cell == 'N':
                    tile = Tile((x,y),'assets/tiles/rock/bottomright.png')
                    self.tiles.add(tile)

                if cell == 'U':
                    self.last_x = x
                    self.last_y = y
                    player_sprite = Player((x,y),self.display_surface,self.create_jump_particles,gems,blue_gems,max_health,current_health,max_stamina,regen_rate,current_stamina,blue_level,red_level,bgems,rgems,damage,speed,current_level,collects,False)
                    self.player.add(player_sprite)
                if cell == 'I':
                    portal_sprite = Portal((x,y-95))
                    self.portal.add(portal_sprite)
                if cell == 'O':
                    col_sprite = Monster_col((x,y))
                    self.monster_col.add(col_sprite)
                if cell == 'J':
                    monster_sprite = Abelha((x,y))
                    self.monster.add(monster_sprite)
                if cell == 'K':
                    monster_sprite = Caramujo((x,y+10))
                    self.monster.add(monster_sprite)
                if cell == 'L':
                    monster_sprite = Javali((x,y))
                    self.monster.add(monster_sprite)
                if cell == 'M':
                    gem_sprite = Gem((x,y+5),'blue')
                    self.bgems.add(gem_sprite)
                if cell == ',':
                    gem_sprite = Gem((x,y+5),'red')
                    self.bgems.add(gem_sprite)
                if cell == '.':
                    col_sprite = Monster_col((x,y))
                    self.fly_col.add(col_sprite)

                if cell == '1':
                    collect_sprite = Collectable((x,y),'fang')
                    self.collectables.add(collect_sprite)
                if cell == '2':
                    collect_sprite = Collectable((x,y),'eye')
                    self.collectables.add(collect_sprite)
                if cell == '3':
                    collect_sprite = Collectable((x,y),'fur')
                    self.collectables.add(collect_sprite)
                if cell == '4':
                    collect_sprite = Collectable((x,y),'scalp')
                    self.collectables.add(collect_sprite)
                if cell == '5':
                    collect_sprite = Collectable((x,y),'blood')
                    self.collectables.add(collect_sprite)
                if cell == '6':
                    collect_sprite = Collectable((x,y),'ring')
                    self.collectables.add(collect_sprite)
                
                if cell == '+':
                    boss_sprite = Boss((x,y-60),self.player.sprite.collectables)
                    self.boss.add(boss_sprite)

    def get_player_on_ground(self):
        if self.player.sprite.on_ground:
            self.player_on_ground = True
        else:
            self.player_on_ground = False

    def check_portal_collision(self):
        player = self.player.sprite
        portal = self.portal.sprite
        collide = pygame.sprite.spritecollide(player,self.portal,False)
        if collide:
            player.rect.x = portal.rect.x
            player.status = 'portal'
        if player.status == 'portal':
            player.rect.y = portal.rect.y + 45
            player.opac -= 4
            player.vel_animacao = 0.2
            
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x

        if player_x < screen_width/4 and direction_x < 0:
            self.world_shift = player.cur_speed
            player.speed = 0
        elif player_x > screen_width-(screen_width/4) and direction_x > 0:
            self.world_shift = -player.cur_speed
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = player.cur_speed

    def check_collect(self):
        player = self.player.sprite
        collects = pygame.sprite.spritecollide(player,self.collectables,True)
        if collects:
            self.gem_sound.play()
            for col in collects:
                if col.name == 'fang':
                    self.dialogue_text = 1
                if col.name == 'eye':
                    self.dialogue_text = 2
                if col.name == 'fur':
                    self.dialogue_text = 3
                if col.name == 'scalp':
                    self.dialogue_text = 4
                if col.name == 'blood':
                    self.dialogue_text = 5
                if col.name == 'ring':
                    self.dialogue_text = 6
                    player.speed += 1
                    player.cur_speed += 2
                    player.max_stamina += 10
                    player.current_stamina += 10
                    player.attack_damage += 5
                    player.max_health += 10
                    player.current_health += 10
                self.game_state = 'DIALOGUE'
                player.collectables.append(col.name)
 
    def horizontal_movement_collision(self):
        player = self.player.sprite
        if player.status != 'portal':
            player.rect.x += player.direction.x * player.speed
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.x < 0:
                        player.rect.left = sprite.rect.right
                        player.on_left = True
                        self.current_x = player.rect.left
                    elif player.direction.x > 0:
                        player.rect.right = sprite.rect.left
                        player.on_right = True
                        self.current_x = player.rect.right

            for sprite in self.monster.sprites():
                if sprite.name == 'caramujo' and sprite.status == 'hidden':
                    if sprite.rect.colliderect(player.rect):
                        if player.direction.x < 0:
                            player.rect.left = sprite.rect.right
                            player.on_left = True
                            self.current_x = player.rect.left
                        elif player.direction.x > 0:
                            player.rect.right = sprite.rect.left
                            player.on_right = True
                            self.current_x = player.rect.right

            if player.on_left and (player.rect.left < self.current_x or player.direction.x >= 0):
                player.on_left = False
            if player.on_right and (player.rect.right > self.current_x or player.direction.x <= 0):
                player.on_right = False
       
    def enemy_horizontal_collisions(self):
        for enemy in self.monster.sprites():
            if enemy.type == 'terrestre':
                enemy.rect.x += enemy.direction.x * enemy.speed
                for collision in self.monster_col.sprites():
                    if collision.rect.colliderect(enemy.rect):
                        enemy.direction.x *= -1
                        if not enemy.facing_right:
                            enemy.facing_right = True
                        else:
                            enemy.facing_right = False

    def enemy_vertical_collisions(self):
        for enemy in self.monster.sprites():
            if enemy.type == 'voador':
                enemy.rect.y += enemy.direction.y * enemy.speed
                for collision in self.fly_col.sprites():
                    if collision.rect.colliderect(enemy.rect):
                        enemy.direction.y *= -1
      
    def vertical_movement_collision(self):
        player = self.player.sprite
        if player.status != 'portal':
            player.apply_gravity()
            for sprite in self.tiles.sprites():
                if sprite.rect.colliderect(player.rect):
                    if player.direction.y > 0:
                        player.rect.bottom = sprite.rect.top
                        player.direction.y = 0
                        player.on_ground = True
                    elif player.direction.y < 0:
                        player.rect.top = sprite.rect.bottom
                        player.direction.y = 0
                        player.on_ceiling = True

            if self.monster:
                for sprite in self.monster.sprites():
                    if sprite.name == 'caramujo' and sprite.status == 'hidden':
                        if sprite.rect.colliderect(player.rect):
                            if player.direction.y > 0:
                                player.rect.bottom = sprite.rect.top
                                player.direction.y = 0
                                player.on_ground = True
                            elif player.direction.y < 0:
                                player.rect.top = sprite.rect.bottom
                                player.direction.y = 0
                                player.on_ceiling = True
                    
            if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
                player.on_ground = False
            if player.on_ceiling and player.direction.y > 0:
                player.on_ceiling = False

    def check_attack_collision(self):
        player = self.player.sprite
        if player.attacking or player.fire_attack or player.dodge:
            collided_enemies = pygame.sprite.spritecollide(player,self.monster,False)
            if collided_enemies:
                for enemy in collided_enemies:
                    if not enemy.hit and enemy.status != 'hidden':
                        if enemy.name == 'javali' or enemy.name == 'abelha':
                            enemy.direction *=-1
                        elif enemy.name == 'caramujo':
                            enemy.speed = 0
                        enemy.life -= player.attack_damage/10
                        enemy.hit = True
                        enemy.hit_time = pygame.time.get_ticks()

        else:
            for fireball in self.fireball.sprites():
                collided = pygame.sprite.spritecollide(fireball,self.monster,False)
                if collided:
                    for enemy in collided:
                        if not enemy.hit and enemy.status != 'hidden':
                            if enemy.name == 'javali':
                                enemy.direction *=-1
                            elif enemy.name == 'caramujo':
                                enemy.speed = 0
                            enemy.life -= (player.attack_damage*1.5)/10
                            enemy.hit = True
                            enemy.hit_time = pygame.time.get_ticks()
            collided_enemies = pygame.sprite.spritecollide(player,self.monster,False)
            if collided_enemies:
                for enemy in collided_enemies:
                    if not player.invincible and not player.attacking and not player.fire_attack:
                        if enemy.type == 'voador':
                            self.player_damage(5)
                            player.invincible = True
                        elif enemy.type == 'terrestre' and enemy.status != 'hidden':
                            self.player_damage(5)
                            player.invincible = True
                        player.hurt_time = pygame.time.get_ticks()
    
    def player_fireball(self):
        player = self.player.sprite
        if player.fire_attack and not self.fireball:
            if player.facing_right:
                fireball = Fireball((player.rect.x + (player.image.get_width()),player.rect.y + (player.image.get_height()-20)),True,5,300)
            else:
                fireball = Fireball((player.rect.x,player.rect.y + (player.image.get_height()-20)),False,-5,300)
            self.fireball.add(fireball)
            self.fireball_sound.play()
    
    def fireball_cd(self):
        for fireball in self.fireball.sprites():
            fireball.range -= 5
            if fireball.range <= 0:
                fireball.kill()

    def check_snail_hide(self):
        player = self.player.sprite
        for enemy in self.monster.sprites():
             if enemy.name == 'caramujo':
                if player.rect.x >= enemy.rect.x-100 and player.rect.x <= enemy.rect.x + 100:
                    if not enemy.hidden:
                        enemy.hidden = True
                else:
                    if enemy.hidden:
                        enemy.hidden = False
                        enemy.unhiding = True
                        enemy.hide_time = pygame.time.get_ticks()
                    else:
                        enemy.status = 'slide'
                    
    def restart(self):
        self.setup_level(level0_map,0,20,100,100,100,0.5,100,0,0,0,0,10,8,0,[],False)
        self.current_level = 0

    def check_game_over(self):
        player = self.player.sprite
        if player.current_health <= 0:
            player.status = 'dead'
            player.game_over -=1
            player.speed = 0
            if player.game_over <= 0:
                self.game_state = 'GAME_OVER'
                if not player.fade:
                    player.fade = True
                    self.fadeout()
                    self.fadein()
                self.hud.gameover()

    def next_level(self):
        player = self.player.sprite
        if player.level == self.current_level + 1:
            self.load()
            if player.level == 1:
                self.setup_level(level1_map,player.gems,player.blue_gems,player.max_health,player.current_health,player.max_stamina,player.stamina_regen_rate,player.current_stamina,player.blue_level,player.red_level,player.bgems,player.rgems,player.attack_damage,player.speed,player.level,player.collectables,False) 
            elif player.level == 2:
                self.setup_level(level2_map,player.gems,player.blue_gems,player.max_health,player.current_health,player.max_stamina,player.stamina_regen_rate,player.current_stamina,player.blue_level,player.red_level,player.bgems,player.rgems,player.attack_damage,player.speed,player.level,player.collectables,False)
            elif player.level == 3:
                self.setup_level(level3_map,player.gems,player.blue_gems,player.max_health,player.current_health,player.max_stamina,player.stamina_regen_rate,player.current_stamina,player.blue_level,player.red_level,player.bgems,player.rgems,player.attack_damage,player.speed,player.level,player.collectables,False)
            elif player.level == 4:
                self.setup_level(level4_map,player.gems,player.blue_gems,player.max_health,player.current_health,player.max_stamina,player.stamina_regen_rate,player.current_stamina,player.blue_level,player.red_level,player.bgems,player.rgems,player.attack_damage,player.speed,player.level,player.collectables,False)
            elif player.level == 5:
                self.setup_level(final_level_map,player.gems,player.blue_gems,player.max_health,player.current_health,player.max_stamina,player.stamina_regen_rate,player.current_stamina,player.blue_level,player.red_level,player.bgems,player.rgems,player.attack_damage,player.speed,player.level,player.collectables,False)
            
            self.current_level += 1
            
    def fall(self):
        player = self.player.sprite
        if player.rect.y > screen_height:
            self.load()
            self.player_damage(10)
            player.rect.x = self.last_x
            player.rect.y = self.last_y
                    
    def fadeout(self):
        fadeout = pygame.Surface((screen_width, screen_height))
        fadeout = fadeout.convert()
        fadeout.fill('#000000')
        self.font = pygame.font.Font('assets/UI/ARCADEPI.TTF',20)
        for i in range(255):
            fadeout.set_alpha(i)
            self.display_surface.blit(fadeout, (0, 0))
            pygame.display.update()

    def load(self):
        fadeout = pygame.Surface((screen_width, screen_height))
        fadeout = fadeout.convert()
        fadeout.fill('#000000')
        self.font = pygame.font.Font('assets/UI/ARCADEPI.TTF',20)
        for i in range(255):
            fadeout.set_alpha(i)
            self.display_surface.blit(fadeout, (0, 0))
            loading = self.font.render('CARREGANDO...',False,'#DDDDDD')
            loading_rect = loading.get_rect(midleft = ((screen_width)-250,(screen_height)-50))
            self.display_surface.blit(loading,loading_rect)
            pygame.display.update()
        fadein = pygame.Surface((screen_width, screen_height))
        fadein = fadein.convert()
        fadein.fill('#000000')
        self.font = pygame.font.Font('assets/UI/ARCADEPI.TTF',20)
        for j in range(255):
            fadein.set_alpha(255-j)
            self.display_surface.blit(fadein, (0,0))
            loading2 = self.font.render('CARREGANDO...',False,'#DDDDDD')
            loading_rect2 = loading2.get_rect(midleft = ((screen_width)-250,(screen_height)-50))
            self.display_surface.blit(loading2,loading_rect2)
            pygame.display.update()

    def fadein(self):
        fadein = pygame.Surface((screen_width, screen_height))
        fadein = fadein.convert()
        fadein.fill('#000000')
        self.font = pygame.font.Font('assets/UI/ARCADEPI.TTF',20)
        for i in range(0,255,2):
            fadein.set_alpha(255-i)
            self.display_surface.blit(fadein, (0,0))
            pygame.display.update()

    def check_enemy_death(self):
        player = self.player.sprite
        for enemy in self.monster:
            if enemy.life < 0:
                    enemy.kill()
                    player.gems += 1
                    player.rgems += 1
                    player.blue_gems -= 1
                    if player.current_health < player.max_health:
                        player.current_health += 5
                        if player.current_health > player.max_health:
                            player.current_health = player.max_health

    def level_up(self):
        player = self.player.sprite
        if player.gems >= 20:
            player.level_up = True
            player.level_up_time = pygame.time.get_ticks()
            if player.bgems > player.rgems:
                player.last_level = 'blue'
                player.blue_level +=1
                player.speed += 1
                player.cur_speed += 1
                player.max_stamina += 10
                player.current_stamina += 10
                player.current_health = player.max_health
            elif player.bgems < player.rgems:
                player.last_level = 'red'
                player.red_level += 1
                player.attack_damage += 5
                player.max_health += 10
                player.current_health = player.max_health
            else:
                player.last_level = 'both'
                player.red_level += 1
                player.blue_level += 1
                player.max_stamina += 20
                player.current_stamina += 20
                player.max_health += 20
                player.current_health = player.max_health
            player.gems = 0
            player.bgems = 0
            player.rgems = 0
            player.blue_gems = 20

    def check_gem_collisions(self):
        player = self.player.sprite
        collided_gems = pygame.sprite.spritecollide(player,self.bgems,True)
        if collided_gems:
            self.gem_sound.play()
            for gem in collided_gems:
                self.last_x = gem.rect.x
                self.last_y = gem.rect.y
                player.gems+=1
                if gem.color == 'red':
                    player.blue_gems -=1
                    player.rgems += 1
                    
                else:
                    player.blue_gems +=1
                    player.bgems +=1
                    if player.current_stamina < player.max_stamina:
                        player.current_stamina += 10
                        if player.current_stamina > player.max_stamina:
                            player.current_stamina = player.max_stamina

    def player_damage(self,amount):
        player = self.player.sprite
        player.current_health -= amount
        self.hit_sound.play()

    def get_inputs(self):
        keys = pygame.key.get_pressed()
        if self.game_state == 'ENDGAME':
            if keys[pygame.K_ESCAPE]:
                exit(1)
        if self.game_state == 'INGAME':
            if keys[pygame.K_q]:
                self.menu_sound.play()
                self.game_state = 'SKILL_MENU'
        elif self.game_state == 'SKILL_MENU':
            if keys[pygame.K_ESCAPE]:
                self.menu_sound.play()
                self.game_state = 'INGAME'
        if self.game_state == 'INGAME':
            if keys[pygame.K_e]:
                self.menu_sound.play()
                self.game_state = 'COLLECT_MENU'
            if keys[pygame.K_d]:
                self.game_state = 'DIALOGUE'
                self.cutscene.in_dialogue = True
        elif self.game_state == 'COLLECT_MENU':
            if keys[pygame.K_ESCAPE]:
                self.menu_sound.play()
                self.game_state = 'INGAME'
                
        if self.game_state == 'DIALOGUE':
            if keys[pygame.K_ESCAPE]:
                self.menu_sound.play()
                self.game_state = 'INGAME'
                self.cutscene.in_dialogue = False
        if self.game_state == 'GAME_OVER':
            if keys[pygame.K_RETURN]:
                self.restart()
                self.game_state = 'INGAME'
            
    def show_menu(self):
        player_status = self.player.sprite
        if self.game_state == 'SKILL_MENU':
            self.menu.show_status(player_status.max_health,player_status.max_stamina,player_status.bgems,player_status.rgems,player_status.blue_level,player_status.red_level,player_status.attack_damage,player_status.speed)
        if self.game_state == 'COLLECT_MENU':
            self.menu.show_collects(player_status.collectables)
          
    def boss_AI(self):
        boss = self.boss.sprite
        player = self.player.sprite   
        if player.rect.x < boss.rect.x and boss.rect.x-player.rect.x > 100:
            boss.rect.x -= boss.speed
            boss.facing_right = False
        elif player.rect.x > boss.rect.x and player.rect.x-boss.rect.x > 200:
            boss.rect.x += boss.speed
            boss.facing_right = True
        else:
            if not boss.attacking and not boss.attackcooldown:
                boss.attack()
                boss.attackcooldown = True
                boss.attack_time = pygame.time.get_ticks()

    def boss_damage(self):
        boss = self.boss.sprite
        player = self.player.sprite 

        if player.attacking:
            collide = pygame.sprite.spritecollide(player,self.boss,False)
            if collide and not boss.invincible:
                boss.current_hp -= player.attack_damage
                boss.invincible = True
                boss.damage_time = pygame.time.get_ticks()


        if player.fire_attack or player.dodge:
            if boss.fire_resistant:
                collide = pygame.sprite.spritecollide(player,self.boss,False)
                if collide and not boss.invincible:
                    boss.current_hp -= player.attack_damage
                    boss.invincible = True
                    boss.damage_time = pygame.time.get_ticks()

        if boss.attacking:
            collide = pygame.sprite.spritecollide(boss,self.player,False)
            if collide and not player.invincible:
                player.current_health -= boss.damage
                player.invincible = True
                player.hurt_time = pygame.time.get_ticks()

    def run(self):
        player_status = self.player.sprite
        boss = self.boss.sprite

        self.level_up()
        self.next_level()
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        if self.game_state != 'SKILL_MENU' and self.game_state != 'COLLECT_MENU' and self.game_state != 'DIALOGUE' and self.game_state != 'ENDGAME':
            player_status.gravity = 0.8
            self.scroll_x()
            self.portal.update(self.world_shift)

            self.bgems.update(self.world_shift)

            self.check_gem_collisions()

            self.check_attack_collision()

            self.dust_sprite.update(self.world_shift)

            self.monster_col.update(self.world_shift)
            self.fly_col.update(self.world_shift)

            self.collectables.update(self.world_shift)
            self.monster.update(self.world_shift)
            self.fireball.update(self.world_shift)
            self.enemy_horizontal_collisions()
            self.enemy_vertical_collisions()
            self.check_enemy_death()
            self.player_fireball()
            

            self.check_portal_collision()
            self.player.update()
            if self.current_level == 5:
                self.boss_AI()
                self.boss_damage()
                self.boss.update(self.world_shift)
            
            
            self.horizontal_movement_collision()
            self.get_player_on_ground()
            self.vertical_movement_collision()
            self.create_landing_dust()
        else:
            player_status.gravity = 0
            

        self.get_inputs()
        self.monster.draw(self.display_surface)
        self.fireball.draw(self.display_surface)
        self.monster_col.draw(self.display_surface)
        self.dust_sprite.draw(self.display_surface)
        self.portal.draw(self.display_surface)
        self.bgems.draw(self.display_surface)
        self.player.draw(self.display_surface)
        self.boss.draw(self.display_surface)
        self.collectables.draw(self.display_surface)
        if player_status.level_up:
            self.hud.level_up(player_status.last_level)
        self.show_menu()

        self.check_snail_hide()
        self.fireball_cd()
        
        self.check_game_over()
        self.check_collect()
        self.fall()
        if self.game_state != 'GAME_OVER':
            self.hud.show_health(player_status.current_health,player_status.max_health)
            self.hud.show_stamina(player_status.current_stamina,player_status.max_stamina)
            self.hud.show_icon()
            self.hud.show_icons()
            self.hud.show_gems(player_status.blue_gems,player_status.gems)
            if self.current_level == 5:
                self.hud.boss_health_bar(boss.current_hp,boss.hp)
            if self.cutscene.text_slide <= 70:
                self.cutscene.prologue()

            elif self.cutscene.text_slide > 70 and player_status.main_menu:
                self.menu.main_menu()
                
            
                
            if self.current_level == 5:
                if boss.current_hp <= 0: 
                    self.dialogue_text = 7
                    self.game_state = 'ENDGAME'
            if self.game_state == 'ENDGAME':
                self.game_music.stop()
                self.menu_music.play(loops=-1)
            if self.game_state == 'DIALOGUE' or self.game_state == 'ENDGAME':
                self.cutscene.dialogue(self.dialogue_text)
                

        
        
        
