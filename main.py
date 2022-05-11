import time

import pygame as pg
import sys

import setting
from setting import *
from intro import Intro
from player import Player
from enemy import Enemy
from mainFunctions import drawText

walkCount = 0

playerlor = Player()
pg.init()
screen = pg.display.set_mode(size)
clock = pygame.time.Clock()
i = 0

class MAIN :

    enemyList = []

    notover = False
    running = True
    intro = Intro()
    isRight = False
    isLeft = False
    isUp = False
    isDown = False

    enemy1 = Enemy('enemy1')

    # 게임시작하자 보이는 화면
    def startView(self):
        pg.init()
        self.screen = pg.display.set_mode(size)
        pg.display.set_caption(TITLE)
        screen.blit(self.intro.introImage, (0, 0))
        drawText("OVERROAD", 90, BLACK, 772, 205)
        drawText("OVERROAD", 90, WHITE, 770, 200)
        drawText("Press Eny Key...", 40, WHITE, 770, 700)
        pg.display.flip()
        self.wait_for_key()

    def endView(self):
        screen.blit(self.intro.introImage, (0, 0))
        drawText("GAME OVER...", 90, BLACK, 772, 205)
        pg.display.flip()

    # 키입력 받기
    def wait_for_key(self):
        wating = True
        while wating :
            for event in pg.event.get() :
                if event.type == pg.KEYUP :
                    wating = False

    # 메인 게임
    def mainGame(self):
        self.enemyList.append(self.enemy1)
        screen.blit(setting.MAPIMG, (0, 0))
        if setting.playerX < 0:
            setting.playerX = 0
        elif setting.playerX > setting.size[0] - 30:
            setting.playerX = setting.size[0] - 30

        if setting.playerY < 0:
            setting.playerY = 0
        elif setting.playerY > setting.size[1] - 55:
            setting.playerY = setting.size[1] - 55
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        key_event = pg.key.get_pressed()
        if key_event[pg.K_UP]:
            self.isUp = True
            self.playerUpSprite()
            playerlor.playerMoveUP()
        elif key_event[pg.K_DOWN]:
            self.isDown = True
            self.playerDownSprite()
            playerlor.playerMoveDOWN()
        else :
            screen.blit(PLAYERIMG, (setting.playerX, setting.playerY))

        if key_event[pg.K_LEFT]:
            self.isLeft = True
            self.playerLeftSprite()
            playerlor.playerMoveLEFT()

        if key_event[pg.K_RIGHT]:
            self.isRight = True
            self.playerRightSprite()
            playerlor.playerMoveRIGHT()


        if key_event[pg.K_SPACE]:
            self.enemy1.attack()
            screen.blit(ATTACKIMG, (setting.playerX + 35, setting.playerY+20))
            screen.blit(ATTACKIMG, (setting.playerX - 95, setting.playerY + 20))

        self.enemy1.enemyMove()
        self.Crash()

    def playerRightSprite(self) :
        global walkCount

        if walkCount >= 5:
            walkCount = 0

        if self.isRight == True :
            screen.blit(playerlor.rightWalk[walkCount], (setting.playerX, setting.playerY))
            walkCount += 1

    def playerLeftSprite(self) :
        global walkCount

        if walkCount >= 5:
            walkCount = 0

        if self.isLeft == True :
            screen.blit(playerlor.leftWalk[walkCount], (setting.playerX, setting.playerY))
            walkCount += 1

    def playerUpSprite(self):
        global walkCount

        if walkCount >= 5:
            walkCount = 0

        if self.isUp == True :
            screen.blit(playerlor.leftWalk[walkCount], (setting.playerX, setting.playerY))
            walkCount += 1

    def playerDownSprite(self):
        global walkCount

        if walkCount >= 5:
            walkCount = 0

        if self.isDown == True :
            screen.blit(playerlor.leftWalk[walkCount], (setting.playerX, setting.playerY))
            walkCount += 1

    def Crash(self):
        playerRect = setting.PLAYERIMG.get_rect()
        playerRect.left = setting.playerX
        playerRect.top = setting.playerY

        enemyRect = Enemy.moveEnemy[0].get_rect()
        enemyRect.left = setting.enemyX
        enemyRect.top = setting.enemyY

        if playerRect.colliderect(enemyRect):
            time.sleep(3)
            self.endView()
            self.running = False
            self.wait_for_key()

game = MAIN()

game.startView()
while game.running :
    game.mainGame()
    game.Crash()
    pg.display.update()
game.endView()