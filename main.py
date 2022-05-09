import pygame as pg
import sys

import setting
import random
from setting import *
from intro import Intro
from player import Player
from enemy import Enemy
from mainFunctions import drawText

walkCount = 0

player = Player()
pg.init()
screen = pg.display.set_mode(size)
clock = pygame.time.Clock()
i = 0

class MAIN :
    swingCount = 0

    running = True
    intro = Intro()
    isRight = False
    isLeft = False
    isUp = False
    isDown = False

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

    # 키입력 받기
    def wait_for_key(self):
        wating = True
        while wating :
            for event in pg.event.get() :
                if event.type == pg.KEYUP :
                    wating = False

    # 메인 게임
    def mainGame(self):
        walkCount = 0

        screen.blit(setting.MAPIMG, (0, 0))
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        key_event = pg.key.get_pressed()
        if key_event[pg.K_UP]:
            self.isUp = True
            self.playerUpSprite()
            player.playerMoveUP()
        elif key_event[pg.K_DOWN]:
            self.isDown = True
            self.playerDownSprite()
            player.playerMoveDOWN()
        else :
            screen.blit(PLAYERIMG, (setting.playerX, setting.playerY))

        if key_event[pg.K_LEFT]:
            self.isLeft = True
            self.playerLeftSprite()
            player.playerMoveLEFT()

        if key_event[pg.K_RIGHT]:
            self.isRight = True
            self.playerRightSprite()
            player.playerMoveRIGHT()


        if key_event[pg.K_SPACE]:
            player.attack()
            screen.blit(ATTACKIMG, (setting.playerX + 35, setting.playerY+20))
            screen.blit(ATTACKIMG, (setting.playerX - 95, setting.playerY + 20))

    def playerRightSprite(self) :
        global walkCount

        if walkCount >= 5:
            walkCount = 0

        if self.isRight == True :
            screen.blit(player.rightWalk[walkCount], (setting.playerX, setting.playerY))
            walkCount += 1

    def playerLeftSprite(self) :
        global walkCount

        if walkCount >= 5:
            walkCount = 0

        if self.isLeft == True :
            screen.blit(player.leftWalk[walkCount], (setting.playerX, setting.playerY))
            walkCount += 1

    def playerUpSprite(self):
        global walkCount

        if walkCount >= 5:
            walkCount = 0

        if self.isUp == True :
            screen.blit(player.leftWalk[walkCount], (setting.playerX, setting.playerY))
            walkCount += 1

    def playerDownSprite(self):
        global walkCount

        if walkCount >= 5:
            walkCount = 0

        if self.isDown == True :
            screen.blit(player.leftWalk[walkCount], (setting.playerX, setting.playerY))
            walkCount += 1

    # def addSwingCount(self) :
    #
    #     self.swingCount += 1
    #     if self.swingCount >= 2:
    #         self.swingCount = 0
    #
    # def enemyMoveSprtie(self):
    #     schedule.every(1).seconds.do(self.addSwingCount)
    #     schedule.run_pending()
    #     screen.blit(Enemy.moveEnemy[self.swingCount], (700, 600))


game = MAIN()

game.startView()

while True :
    game.mainGame()
    screen.blit(Enemy.moveEnemy[1], (random.randint(1, 1500), random.randint(1, 850)))

    pg.display.update()