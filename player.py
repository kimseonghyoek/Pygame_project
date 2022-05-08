import pygame as pg

import setting
from setting import *
from main import screen

class Peadsf :

    walkCount = 0

    pg.init()
    # screen = pg.display.set_mode(size)

    rightWalk = [pg.image.load('user1.png'), pg.image.load('user2.png'), pg.image.load('user3.png')]
    rightWalk = pg.transform.scale(rightWalk[0], (30, 55)), pg.transform.scale(rightWalk[1], (30, 55)), pg.transform.scale(rightWalk[2], (30, 55))

    # 플레이어 그리기
    def drawPlayer(self):
        self.screen.blit(PLAYERIMG, (playerX, playerY))

    def playerMoveUP(self):
        setting.playerY -= 0.25
        print('up', setting.playerY)
    def playerMoveDOWN(self):
        setting.playerY += 0.25
        print('down', setting.playerY)
    def playerMoveLEFT(self):
        setting.playerX -= 0.25
        print('left', setting.playerX)
    def playerMoveRIGHT(self):
        global walkCount
        if walkCount >= 3 :
            walkCount = 0
        screen.blit(self.rightWalk[walkCount], (setting.playerX, setting.playerY))
        setting.playerX += 0.25
        print('right', setting.playerX)

    # 플레이어 공격
    def attack(self):
        # 아직은 구조가 생각이..
        return 0