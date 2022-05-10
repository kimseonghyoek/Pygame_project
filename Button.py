import pygame
from setting import size

def WAITFORKEY() :
    waiting = True
    while waiting :
        for event in pygame.event.get() :
            if event.type == pygame.KEYUP :
                waiting = False
                print('key event!!!')