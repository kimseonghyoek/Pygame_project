import pygame as pg
import sys
import setting
from setting import *
from intro import Intro
from player import Player

player = Player()
pg.init()
screen = pg.display.set_mode(size)

class MAIN :
    gameState = True
    running = True
    clock = pygame.time.Clock()
    intro = Intro()

    def init(self):
        pg.init()
        self.screen = pg.display.set_mode(size)
        pg.display.set_caption(TITLE)
        screen.blit(self.intro.introImage, (0, 0))
        self.drawText("OVERROAD", 90, BLACK, 772, 205)
        self.drawText("OVERROAD", 90, WHITE, 770, 200)
        self.drawText("Press key 1...", 40, WHITE, 770, 700)
        pg.display.flip()
        pg.display.update()

    def events(self):
        # 게임 루프가 True일 경우
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.gameState = False
                self.running = False
            elif event.type == pg.KEYUP :
                if event.key == pg.K_1 :
                    self.mainGame()
                    print("One Coin!!")
                elif event.key == pg.K_UP :
                    player.playerMoveUP()
                    player.drawPlayer()
                elif event.key == pg.K_DOWN :
                    player.playerMoveDOWN()
                    player.drawPlayer()
                elif event.key == pg.K_ESCAPE :
                    print('ESC')
                    self.esc()


    def new(self):
        self.startGame()

    # 게임 시작
    def startGame(self):
        while self.gameState :
            player.drawPlayer()
            setting.BGM.play(-1)
            self.events()

    # 메인 게임
    def mainGame(self):
        self.screen.blit(setting.MAPIMG, (0, 0))
        player.drawPlayer()
        self.events()
        pg.display.flip()

    def drawText(self, text, size, color, x, y):
        font = pg.font.Font(font_name, size)
        text_suface = font.render(text, True, color)
        text_rect = text_suface.get_rect()
        text_rect.midtop = (x, y)
        self.screen.blit(text_suface, text_rect)
        pg.display.flip()

g = MAIN()
while g.running:
    g.init()
    g.new()