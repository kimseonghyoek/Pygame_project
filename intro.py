import pygame
import setting

class Intro :
    introImage = pygame.image.load("shit.gif")
    introImage = pygame.transform.scale(introImage, (setting.size[0], setting.size[1]))