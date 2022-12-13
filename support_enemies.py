from os import walk
import pygame

def importar_pasta(caminho):
    surface_list = []
    caminhos = []

    for _,__,imagens in walk(caminho):
        for imagem in imagens:
            if imagem != '.DS_Store':
                caminho_completo = caminho + '/' + imagem
                caminhos.append(caminho_completo)
        caminhos.sort()
        for path in caminhos:
            surface = pygame.image.load(path).convert_alpha()
            surface = pygame.transform.scale(surface,((surface.get_width())*1.2,(surface.get_height())*1.2))
            surface_list.append(surface)
    return surface_list
