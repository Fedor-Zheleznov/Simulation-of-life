import pygame

pygame.init()

def events():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()