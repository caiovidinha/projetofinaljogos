from os import walk
import pygame

def importar_pasta(caminho):
    surface_list = []

    for _,__,imagens in walk(caminho):
        for imagem in imagens:
            caminho_completo = caminho + '/' + imagem
            
            
            if imagem != '.DS_Store':
                surface = pygame.image.load(caminho_completo).convert_alpha()
                surface_list.append(surface)
    return surface_list
