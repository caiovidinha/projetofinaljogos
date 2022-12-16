import pygame
from settings import *

class UI:
    def __init__(self,surface):

        self.display_surface = surface

        self.health_bar = pygame.image.load('assets/UI/health_bar.png').convert_alpha()
        self.health_bar = pygame.transform.scale(self.health_bar,(116,12))
        self.health_bar_topleft = (76,20)
        self.boss_bar_topleft = (30,480)
        self.bar_max_width = 116
        self.bar_height = 12

        self.last_level = True

        self.game_over = pygame.image.load('assets/gameoverbg.jpg').convert_alpha()
        self.boss_bar = pygame.image.load('assets/UI/bosslifebar.png').convert_alpha()
        self.boss_bar_frame = pygame.image.load('assets/UI/boss_bar_frame.png').convert_alpha()
        self.boss_bar = pygame.transform.scale(self.boss_bar,(958,25))
        self.boss_bar_frame = pygame.transform.scale(self.boss_bar_frame,(958,25))

        self.stamina_bar = pygame.image.load('assets/UI/stamina_bar.png').convert_alpha()
        self.stamina_bar = pygame.transform.scale(self.stamina_bar,(116,12))
        self.stamina_bar_topleft = (76,33)
        self.bar_max_width = 111
        self.bar_height = 12

        self.bar = pygame.image.load('assets/UI/bar.png').convert_alpha()
        self.bar = pygame.transform.scale(self.bar,(116,12))

        self.gems_bar = pygame.image.load('assets/UI/gemsbar.png').convert_alpha()
        self.gemsbar_max_width = 56

        self.icon = pygame.image.load('assets/UI/icon.png').convert_alpha()
        self.icon = pygame.transform.scale(self.icon,(52,52))

        self.armor = pygame.image.load('assets/UI/armor.png').convert_alpha()
        self.bag = pygame.image.load('assets/UI/bag.png').convert_alpha()
        self.gems = pygame.image.load('assets/UI/gems.png').convert_alpha()

        self.woodbg = pygame.image.load('assets/UI/levelup/woodbg.png').convert_alpha()
        self.woodbg = pygame.transform.scale(self.woodbg,(180,60))

        self.moonbg = pygame.image.load('assets/UI/levelup/moonbg.png').convert_alpha()
        self.moonbg = pygame.transform.scale(self.moonbg,(104,104))

        self.blueup = pygame.image.load('assets/UI/levelup/blueup.png').convert_alpha()
        self.blueup = pygame.transform.scale(self.blueup,(66,66))

        self.redup = pygame.image.load('assets/UI/levelup/redup.png').convert_alpha()
        self.redup = pygame.transform.scale(self.redup,(66,66))

        self.levelup = pygame.image.load('assets/UI/levelup/levelup.png').convert_alpha()
        self.levelup = pygame.transform.scale(self.levelup,(24,21))

        self.font_big = pygame.font.Font('assets/UI/ARCADEPI.TTF',15)
        self.font = pygame.font.Font('assets/UI/ARCADEPI.TTF',13)
        self.font_small = pygame.font.Font('assets/UI/ARCADEPI.TTF',7)

    def gameover(self):
        self.display_surface.blit(self.game_over,(0,0))

    def show_health(self,current_health,full):
        self.display_surface.blit(self.health_bar,(73,20))
        current_health_ratio = current_health/full
        current_bar_width = self.bar_max_width * current_health_ratio
        health_bar_rect = pygame.Rect(self.health_bar_topleft,(current_bar_width,self.bar_height))
        pygame.draw.rect(self.display_surface,'#dc4949',health_bar_rect)
        self.display_surface.blit(self.bar,(73,20))

    def level_up(self,color):
        self.display_surface.blit(self.woodbg,((screen_width/2)-90,(screen_height/2)-30))
        self.display_surface.blit(self.moonbg,((screen_width/2-52),(screen_height/2-124)))
        if color == 'blue':
            self.display_surface.blit(self.blueup,((screen_width/2-33),(screen_height/2)-106))
            sp_up = self.font_big.render('SP+10',False,'#DDDDDD')
            sp_up_rect = sp_up.get_rect(midleft = ((screen_width/2)-75,(screen_height/2)))
            self.display_surface.blit(sp_up,sp_up_rect)
            speed_up = self.font_big.render('SPEED+1',False,'#DDDDDD')
            speed_up_rect = speed_up.get_rect(midleft = ((screen_width/2)-10,(screen_height/2)))
            self.display_surface.blit(speed_up,speed_up_rect)
        elif color == 'red':
            self.display_surface.blit(self.redup,((screen_width/2-33),(screen_height/2)-106))
            hp_up = self.font_big.render('HP+10',False,'#DDDDDD')
            hp_up_rect = hp_up.get_rect(midleft = ((screen_width/2)-80,(screen_height/2)))
            self.display_surface.blit(hp_up,hp_up_rect)
            attack_up = self.font_big.render('ATTACK+5',False,'#DDDDDD')
            attack_up_rect = attack_up.get_rect(midleft = ((screen_width/2)-15,(screen_height/2)))
            self.display_surface.blit(attack_up,attack_up_rect)
        elif color == 'both':
            hp_up = self.font_big.render('HP+20',False,'#DDDDDD')
            hp_up_rect = hp_up.get_rect(midleft = ((screen_width/2)-60,(screen_height/2)))
            self.display_surface.blit(hp_up,hp_up_rect)
            sp_up = self.font_big.render('SP+20',False,'#DDDDDD')
            sp_up_rect = sp_up.get_rect(midleft = ((screen_width/2)+10,(screen_height/2)))
            self.display_surface.blit(sp_up,sp_up_rect)

        self.display_surface.blit(self.levelup,((screen_width/2)-12,(screen_height/2)-83))
        
        

    def show_stamina(self,current_stamina,full):
        self.display_surface.blit(self.stamina_bar,(73,33))
        current_stamina_ratio = current_stamina/full
        current_bar_width = self.bar_max_width * current_stamina_ratio
        stamina_bar_rect = pygame.Rect(self.stamina_bar_topleft,(current_bar_width,self.bar_height))
        pygame.draw.rect(self.display_surface,'#174171',stamina_bar_rect)
        self.display_surface.blit(self.bar,(73,33))
    
    def show_icon(self):
        self.display_surface.blit(self.icon,(20,20))
    
    def show_icons(self):
        self.display_surface.blit(self.armor,(74,46))
        q  = self.font_small.render('Q',False,'#DDDDDD')
        q_rect = q.get_rect(midleft = (77,50))
        self.display_surface.blit(q,q_rect)
         
        self.display_surface.blit(self.bag,(102,46))
        e  = self.font_small.render('E',False,'#DDDDDD')
        e_rect = e.get_rect(midleft = (105,50))
        self.display_surface.blit(e,e_rect)
        
    def show_gems(self,blue_amount,amount):
        self.display_surface.blit(self.gems,(130,46))
        gem_amount_surface = self.font.render(str(amount),False,'#DDDDDD')
        gem_amount_rect = gem_amount_surface.get_rect(midleft = (163,59))
        blue = blue_amount/40
        current_bluebar_width = self.gemsbar_max_width * blue
        

        gems_blue_rect = pygame.Rect((131,47),(current_bluebar_width,25))
    
        gems_red_rect = pygame.Rect((131,47),(self.gemsbar_max_width,25))

        pygame.draw.rect(self.display_surface,'#dc4949',gems_red_rect)
        pygame.draw.rect(self.display_surface,'#174171',gems_blue_rect)
        self.display_surface.blit(self.gems_bar,(130,46))
        self.display_surface.blit(gem_amount_surface,gem_amount_rect)

    def boss_health_bar(self,current_health,full):
        self.display_surface.blit(self.boss_bar,(21,475))
        current_health_ratio = current_health/full
        current_bar_width = 940 * current_health_ratio
        boss_bar_rect = pygame.Rect(self.boss_bar_topleft,(current_bar_width,15))
        pygame.draw.rect(self.display_surface,'#8F0B0B',boss_bar_rect)
        self.display_surface.blit(self.boss_bar_frame,(21,475))
        boss_name = self.font_big.render('A BESTA',False,'#DDDDDD')
        boss_name_rect = boss_name.get_rect(center = ((screen_width/2),470))
        self.display_surface.blit(boss_name,boss_name_rect)