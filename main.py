import pygame as pg
import sys
import setting
from setting import *
from intro import Intro
from player import Player
from mainFunctions import drawText

player = Player()
pg.init()
screen = pg.display.set_mode(size)
clock = pygame.time.Clock()
i = 0

class MAIN :
    running = True
    intro = Intro()

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
            player.playerMoveUP()

        if key_event[pg.K_DOWN]:
            player.playerMoveDOWN()

        if key_event[pg.K_LEFT]:
            player.playerMoveLEFT()

        if key_event[pg.K_RIGHT]:
            player.playerMoveRIGHT()
            screen.blit(player.rightWalk[walkCount], (setting.playerX, setting.playerY))
            walkCount += 1

        if key_event[pg.K_SPACE]:
            player.attack()
            screen.blit(player.rightWalk[walkCount], (setting.playerX, setting.playerY))
            screen.blit(ATTACKIMG, (setting.playerX + 35, setting.playerY+20))
            screen.blit(ATTACKIMG, (setting.playerX - 95, setting.playerY + 20))
        else :
            screen.blit(PLAYERIMG, (setting.playerX, setting.playerY))

game = MAIN()

game.startView()
while True :
    game.mainGame()
    pg.display.update()