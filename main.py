import pygame as pg
import sys
import setting
from setting import *
from intro import Intro
from player import Player

player = Player()
pg.init()
screen = pg.display.set_mode(size)
clock = pygame.time.Clock()

class MAIN :
    gameState = True
    running = True
    intro = Intro()

    # 게임시작하자 보이는 화면
    def startGame(self):
        pg.init()
        self.screen = pg.display.set_mode(size)
        pg.display.set_caption(TITLE)
        screen.blit(self.intro.introImage, (0, 0))
        self.drawText("OVERROAD", 90, BLACK, 772, 205)
        self.drawText("OVERROAD", 90, WHITE, 770, 200)
        self.drawText("Press key 1...", 40, WHITE, 770, 700)
        pg.display.flip()
        pg.display.update()

        while self.gameState :
            setting.BGM.play(-1)
            self.events()

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
                elif event.key == pg.K_DOWN :
                    player.playerMoveDOWN()
                elif event.key == pg.K_ESCAPE :
                    print('ESC')
                    self.esc()

    def new(self):
        self.startGame()
        
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
    dt = clock.tick(30)
    g.startGame()
    g.new()
    player.drawPlayer()