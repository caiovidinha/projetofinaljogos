import pygame
import settings

class Menu:
    def __init__(self,surface):

        self.display_surface = surface
        self.settings = settings

        #skill menu
        self.background = pygame.image.load('assets/menu/skill_menu/background.png')

        self.menu_background = pygame.image.load('assets/menu/skill_menu/skills_menu.png')
        self.menu_background = pygame.transform.scale(self.menu_background,(600,364))

        self.fireball = pygame.image.load('assets/menu/skill_menu/fireball.png')
        self.dodge = pygame.image.load('assets/menu/skill_menu/dodge.png')
        self.dodge = pygame.transform.scale(self.dodge,(32,26))

        self.health_bar = pygame.image.load('assets/menu/skill_menu/health_bar.png').convert_alpha()
        self.health_bar = pygame.transform.scale(self.health_bar,(214,12))
        self.stamina_bar = pygame.image.load('assets/menu/skill_menu/stamina_bar.png').convert_alpha()
        self.stamina_bar = pygame.transform.scale(self.stamina_bar,(214,12))

        self.esc = pygame.image.load('assets/menu/skill_menu/close_icon.png').convert_alpha()
        self.esc = pygame.transform.scale(self.esc,(28,28))

        self.blue_gems = pygame.image.load('assets/menu/skill_menu/blue_gems.png').convert_alpha()
        self.blue_gems = pygame.transform.scale(self.blue_gems,(21,21))
        self.red_gems = pygame.image.load('assets/menu/skill_menu/red_gems.png').convert_alpha()
        self.red_gems = pygame.transform.scale(self.red_gems,(21,21))

        self.skills = pygame.image.load('assets/menu/skill_menu/skill.png')
        self.skills = pygame.transform.scale(self.skills,(32,32))

        self.attack_icon = pygame.image.load('assets/menu/skill_menu/attack_icon.png')
        self.attack_icon = pygame.transform.scale(self.attack_icon,(36,42))
        
        self.speed_icon = pygame.image.load('assets/menu/skill_menu/speed_icon.png')
        self.speed_icon = pygame.transform.scale(self.speed_icon,(42,21))

        self.blue_skills = pygame.image.load('assets/menu/skill_menu/blue_skillup.png')
        self.blue_skills = pygame.transform.scale(self.blue_skills,(32,32))

        self.red_skills = pygame.image.load('assets/menu/skill_menu/red_skillup.png')
        self.red_skills = pygame.transform.scale(self.red_skills,(32,32))

        self.fang = pygame.image.load('assets/collects/fang.png')
        self.fang = pygame.transform.scale(self.fang,(40,40))
        self.eye = pygame.image.load('assets/collects/eye.png')
        self.eye = pygame.transform.scale(self.eye,(40,40))
        self.fur = pygame.image.load('assets/collects/fur.png')
        self.fur = pygame.transform.scale(self.fur,(40,40))
        self.scalp = pygame.image.load('assets/collects/scalp.png')
        self.scalp = pygame.transform.scale(self.scalp,(40,40))
        self.blood = pygame.image.load('assets/collects/blood.png')
        self.blood = pygame.transform.scale(self.blood,(40,40))
        self.ring = pygame.image.load('assets/collects/ring.png')
        self.ring = pygame.transform.scale(self.ring,(40,40))



        self.main_menu_bg = pygame.image.load('assets/menu/main_menu/background.jpg')
        self.main_menu_text = pygame.image.load('assets/menu/main_menu/text.png')
        self.text_opac = 255
        self.decay = True
        
        self.font_big = pygame.font.Font('assets/UI/ARCADEPI.TTF',20)
        self.font = pygame.font.Font('assets/UI/ARCADEPI.TTF',13)
        self.font_small = pygame.font.Font('assets/UI/ARCADEPI.TTF',7)

        #skill menu
        self.background = pygame.image.load('assets/menu/skill_menu/background.png')

        self.collect_background = pygame.image.load('assets/menu/collectables_menu/collectbg.png')
        self.collect_background = pygame.transform.scale(self.collect_background,(496,192))

        self.collected_icon = pygame.image.load('assets/menu/collectables_menu/collected.png')
        self.collected_icon = pygame.transform.scale(self.collected_icon,(64,64))
        
    def show_status(self,max_health,max_stamina,bgems,rgems,blevel,rlevel,player_damage,player_speed):
        
        self.display_surface.blit(self.background,(0,0))
        self.display_surface.blit(self.menu_background,((self.settings.screen_width/2)-300,(self.settings.screen_height/2)-182))
        self.display_surface.blit(self.health_bar,(230,(self.settings.screen_height)-130))
        self.display_surface.blit(self.stamina_bar,(230,(self.settings.screen_height)-110))

        self.display_surface.blit(self.blue_gems,(230,(self.settings.screen_height/2)-150))
        self.display_surface.blit(self.red_gems,(230,(self.settings.screen_height/2)-120))

        self.display_surface.blit(self.attack_icon,(742,(self.settings.screen_height/2)-150))
        self.display_surface.blit(self.speed_icon,(738,(self.settings.screen_height/2)-20))

        self.display_surface.blit(self.esc,(745,(self.settings.screen_height)-130))


        skill_bar_rect = pygame.Rect((230,(self.settings.screen_height/2)-52),(428,7))
        pygame.draw.rect(self.display_surface,'#7F7B7B',skill_bar_rect)
        skill_bar_rect2 = pygame.Rect((230,(self.settings.screen_height/2)+28),(428,7))
        pygame.draw.rect(self.display_surface,'#7F7B7B',skill_bar_rect2)
        
        current_blue_level = 100 * blevel
        blue_level_rect = pygame.Rect((230,(self.settings.screen_height/2)-52),(current_blue_level,7))
        pygame.draw.rect(self.display_surface,'#5075A1',blue_level_rect)
        
        current_red_level = 100 * rlevel
        red_level_rect = pygame.Rect((230,(self.settings.screen_height/2)+28),(current_red_level,7))
        pygame.draw.rect(self.display_surface,'#AC3F3C',red_level_rect)

        
        
        for k in range(230,730,100):
            self.display_surface.blit(self.skills,(k,(self.settings.screen_height/2)+16))
            self.display_surface.blit(self.skills,(k,(self.settings.screen_height/2)-64))

        if blevel >= 0:
            self.display_surface.blit(self.blue_skills,(230,(self.settings.screen_height/2)-64))
        if blevel >= 1:
            self.display_surface.blit(self.blue_skills,(330,(self.settings.screen_height/2)-64))
        if blevel >= 2:
            self.display_surface.blit(self.blue_skills,(430,(self.settings.screen_height/2)-64))
            self.display_surface.blit(self.dodge,(430,(self.settings.screen_height/2)-62))
        if blevel >= 3:
            self.display_surface.blit(self.blue_skills,(530,(self.settings.screen_height/2)-64))
        if blevel >= 4:
            self.display_surface.blit(self.blue_skills,(630,(self.settings.screen_height/2)-64))
        

        
        if rlevel >= 0:
            self.display_surface.blit(self.red_skills,(230,(self.settings.screen_height/2)+16))
        if rlevel >= 1:
            self.display_surface.blit(self.red_skills,(330,(self.settings.screen_height/2)+16))
        if rlevel >= 2:
            self.display_surface.blit(self.red_skills,(430,(self.settings.screen_height/2)+16))
            self.display_surface.blit(self.fireball,(430,(self.settings.screen_height/2)+24))
        if rlevel >= 3:
            self.display_surface.blit(self.red_skills,(530,(self.settings.screen_height/2)+16))
        if rlevel >= 4:
            self.display_surface.blit(self.red_skills,(630,(self.settings.screen_height/2)+16))
        
        

        health = 'MAX HP: ' + str(max_health)
        stamina = 'MAX SP: ' + str(max_stamina)
        blue_gems = 'X ' + str(bgems)
        red_gems = 'X ' + str(rgems)
        damage = str(player_damage)
        speed = str(player_speed)

        esc_amount_surface = self.font.render('ESC',False,'#232323')
        esc_amount_rect = esc_amount_surface.get_rect(midleft = (745,(self.settings.screen_height)-95))
        self.display_surface.blit(esc_amount_surface,esc_amount_rect)

        bgems_amount_surface = self.font.render(str(blue_gems),False,'#000000')
        bgems_amount_rect = bgems_amount_surface.get_rect(midleft = (260,(self.settings.screen_height/2)-140))
        self.display_surface.blit(bgems_amount_surface,bgems_amount_rect)

        damage_amount_surface = self.font_big.render(str(damage),False,'#000000')
        damage_amount_rect = damage_amount_surface.get_rect(center = (760,(self.settings.screen_height/2)-80))
        self.display_surface.blit(damage_amount_surface,damage_amount_rect)

        speed_amount_surface = self.font_big.render(str(speed),False,'#000000')
        speed_amount_rect = speed_amount_surface.get_rect(center = (760,(self.settings.screen_height/2)+30))
        self.display_surface.blit(speed_amount_surface,speed_amount_rect)

        rgems_amount_surface = self.font.render(str(red_gems),False,'#000000')
        rgems_amount_rect = rgems_amount_surface.get_rect(midleft = (260,(self.settings.screen_height/2)-110))
        self.display_surface.blit(rgems_amount_surface,rgems_amount_rect)

        health_amount_surface = self.font.render(str(health),False,'#000000')
        health_amount_rect = health_amount_surface.get_rect(midleft = (450,(self.settings.screen_height)-125))
        self.display_surface.blit(health_amount_surface,health_amount_rect)
        
        stamina_amount_surface = self.font.render(str(stamina),False,'#000000')
        stamina_amount_rect = stamina_amount_surface.get_rect(midleft = (450,(self.settings.screen_height)-105))
        self.display_surface.blit(stamina_amount_surface,stamina_amount_rect)

    def show_collects(self,collects):
        self.display_surface.blit(self.background,(0,0))
        self.display_surface.blit(self.collect_background,((self.settings.screen_width/2)-248,(self.settings.screen_height/2)-96))
        
        self.display_surface.blit(self.esc,(702,(self.settings.screen_height/2)+50))
        esc_amount_surface = self.font.render('ESC',False,'#DDDDDD')
        esc_amount_rect = esc_amount_surface.get_rect(midleft = (702,(self.settings.screen_height/2)+85))
        self.display_surface.blit(esc_amount_surface,esc_amount_rect)
        

        for item in collects:
            
            if item == 'fang':
                self.display_surface.blit(self.collected_icon,(292,(self.settings.screen_height/2)-80))
                self.display_surface.blit(self.fang,(305,(self.settings.screen_height/2)-70))
            if item == 'eye':
                self.display_surface.blit(self.collected_icon,(440,(self.settings.screen_height/2)-80))
                self.display_surface.blit(self.eye,(451,(self.settings.screen_height/2)-69))
            if item == 'fur':
                self.display_surface.blit(self.collected_icon,(588,(self.settings.screen_height/2)-80))
                self.display_surface.blit(self.fur,(605,(self.settings.screen_height/2)-72))
            if item == 'scalp':
                self.display_surface.blit(self.collected_icon,(292,(self.settings.screen_height/2)+4))
                self.display_surface.blit(self.scalp,(303,(self.settings.screen_height/2)+14))
            if item == 'blood':
                self.display_surface.blit(self.collected_icon,(440,(self.settings.screen_height/2)+4))
                self.display_surface.blit(self.blood,(452,(self.settings.screen_height/2)+14))
            if item == 'ring':
                self.display_surface.blit(self.collected_icon,(588,(self.settings.screen_height/2)+4))
                self.display_surface.blit(self.ring,(600,(self.settings.screen_height/2)+14))

        
    def main_menu(self):
        self.display_surface.blit(self.main_menu_bg,(0,0))
        self.display_surface.blit(self.main_menu_text,(0,0))
        self.main_menu_text.set_alpha(self.text_opac)
        if self.decay:
            self.text_opac -= 10
            if self.text_opac <= 0:
                self.decay = False
            
        else:
            self.text_opac += 10
            
            if self.text_opac >= 255:
                self.decay = True