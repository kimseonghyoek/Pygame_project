import pygame as pg
from setting import size, BLACK
from intro import text

class GameMenu :
    startScreen = pg.display.set_mode(size)
    font_name = 'DEMON_NI.ttf'



    def M_SHOW_START_SCREEN(self):
        self.startScreen.fill(BLACK)