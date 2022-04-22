import pygame as pg

import setting
from setting import *

class Player :

    pg.init()
    screen = pg.display.set_mode(size)

    # 플레이어 그리기
    def drawPlayer(self):
        self.screen.blit(PLAYERIMG, (playerX, playerY))
        pg.display.update()

    def playerMoveUP(self):
        setting.playerY += 2.5
        print('up', setting.playerY)

    def playerMoveDOWN(self):
        setting.playerY -= 2.5
        print('down', setting.playerY)
