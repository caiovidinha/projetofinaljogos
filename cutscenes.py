import pygame
import settings

class Cutscene:
    def __init__(self,surface):

        self.display_surface = surface
        self.settings = settings
        self.in_dialogue = False
        


        self.prologue_background = pygame.image.load('assets/cutscenes/prologo/background.jpg')
        self.prologue_frame = pygame.image.load('assets/cutscenes/prologo/frame.png')
        self.prologue_text = pygame.image.load('assets/cutscenes/prologo/text.png')
        self.text_slide = 70
        self.font = pygame.font.Font('assets/UI/ARCADEPI.TTF',20)

        self.dialogue_1 = pygame.image.load('assets/cutscenes/dialogo/background.jpg')

    def prologue(self):
        self.display_surface.blit(self.prologue_background,(0,0))
        
        if self.text_slide > 50:
            self.display_surface.blit(self.prologue_text,(0,50))
        else:
            self.display_surface.blit(self.prologue_text,(0,self.text_slide))
        self.text_slide -=2
        if self.text_slide < -850:
            self.text_slide = 71
        self.display_surface.blit(self.prologue_frame,(0,0))

    def dialogue(self,text):
        # if text == 1:
        #     self.display_surface.blit(self.dialogue_1,(0,520-170))
        pass


