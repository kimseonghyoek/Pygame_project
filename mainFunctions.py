import pygame as pg
from setting import *
from main import MAIN, screen

class Function :

    # text를 써주는 기능
    def drawText(self, text, size, color, x, y):
        font = pg.font.Font(font_name, size)
        text_suface = font.render(text, True, color)
        text_rect = text_suface.get_rect()
        text_rect.midtop = (x, y)
        screen.blit(text_suface, text_rect)
        pg.display.flip()