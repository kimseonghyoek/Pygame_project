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
        setting.playerY -= 0.35
        print('up', setting.playerY)
    def playerMoveDOWN(self):
        setting.playerY += 0.35
        print('down', setting.playerY)
    def playerMoveLEFT(self):
        setting.playerX -= 0.35
        print('left', setting.playerX)
    def playerMoveRIGHT(self):
        setting.playerX += 0.35
        print('right', setting.playerX)

    # 플레이어 공격
    def attack(self):
        # 아직은 구조가 생각이..
        return 0