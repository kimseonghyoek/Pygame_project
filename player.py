import pygame as pg

import setting
from setting import *

class Player :

    pg.init()
    screen = pg.display.set_mode(size)

    # 플레이어 그리기
    def drawPlayer(self):
        self.screen.blit(PLAYERIMG, (playerX, playerY))

    def playerMoveUP(self):
        setting.playerY += 2.5
        print('up', setting.playerY)
        pg.display.flip()
    def playerMoveDOWN(self):
        setting.playerY -= 2.5
        print('down', setting.playerY)

    def playerMoveRight(self):
        setting.playerX -= 2.5
        print('right', setting.playerX)

    def playerMoveRight(self):
        setting.playerX -= 2.5
        print('right', setting.playerX)