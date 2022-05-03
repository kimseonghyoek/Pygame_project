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
        drawText("Press key 1...", 40, WHITE, 770, 700)
        pg.display.flip()
        self.wait_for_key()

    def events(self):
        # 게임 루프가 True일 경우
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.running = False
            elif event.type == pg.KEYDOWN :
                if event.key == pg.K_1 :
                    self.mainGame()
                elif event.key == pg.K_ESCAPE :
                    self.running = False

    # 키입력 받기
    def wait_for_key(self):
        wating = True
        while wating :
            for event in pg.event.get() :
                if event.type == pg.KEYUP :
                    wating = False

    # 메인 게임
    def mainGame(self):
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

game = MAIN()

game.startView()
while True :
    game.mainGame()
    screen.blit(PLAYERIMG, (setting.playerX, setting.playerY))
    pg.display.update()