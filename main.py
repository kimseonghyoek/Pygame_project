import pygame as pg
import sys

import setting
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

    enemyList = []

    notover = False
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

        walkCount = 0
        screen.blit(setting.MAPIMG, (0, 0))
        self.enemyMove()
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
            self.attack()
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

    def enemyMove(self):
        global enemy1
        maxX = 1410
        maxY = 760
        minX = 10
        minY = 10

        if setting.enemyX >= maxX :
            setting.enemyX = random.randint(10, 1400)
        elif setting.enemyX <= minX :
            setting.enemyX = random.randint(10, 1400)
        if setting.enemyX2 >= maxX :
            setting.enemyX2 = random.randint(10, 1400)
        elif setting.enemyX2 <= minX :
            setting.enemyX2 = random.randint(10, 1400)
        if setting.enemyX3 >= maxX :
            setting.enemyX3 = random.randint(10, 1400)
        elif setting.enemyX3 <= minX :
            setting.enemyX3 = random.randint(10, 1400)
        if setting.enemyX4 >= maxX :
            setting.enemyX4 = random.randint(10, 1400)
        elif setting.enemyX4 <= minX :
            setting.enemyX4 = random.randint(10, 1400)
        if setting.enemyY >= maxY :
            setting.enemyY = random.randint(10, 750)
        elif setting.enemyY <= minY :
            setting.enemyY = random.randint(10, 750)
        if setting.enemyY2 >= maxY :
            setting.enemyY2 = random.randint(10, 750)
        elif setting.enemyY2 <= minY :
            setting.enemyY2 = random.randint(10, 750)
        if setting.enemyY3 >= maxY :
            setting.enemyY3 = random.randint(10, 750)
        elif setting.enemyY3 <= minY :
            setting.enemyY3 = random.randint(10, 750)
        if setting.enemyY4 >= maxY :
            setting.enemyY4 = random.randint(10, 750)
        elif setting.enemyY4 <= minY :
            setting.enemyY4 = random.randint(10, 750)

        setting.enemyX += 0.35
        setting.enemyX2 -= 0.35
        setting.enemyX3 += 0.35
        setting.enemyX4 -= 0.35
        setting.enemyY += 0.35
        setting.enemyY2 += 0.35
        setting.enemyY3 -= 0.35
        setting.enemyY4 += 0.35


        enemy1 = screen.blit(Enemy.moveEnemy[0], (setting.enemyX, setting.enemyY)),
        screen.blit(Enemy.moveEnemy[random.randint(0, 1)], (setting.enemyX2, setting.enemyY3)),
        screen.blit(Enemy.moveEnemy[random.randint(0, 1)], (setting.enemyX3, setting.enemyY2)),
        screen.blit(Enemy.moveEnemy[random.randint(0, 1)], (setting.enemyX4, setting.enemyY4)),
        screen.blit(Enemy.moveEnemy[random.randint(0, 1)], (setting.enemyX2, setting.enemyY)),
        screen.blit(Enemy.moveEnemy[random.randint(0, 1)], (setting.enemyX3, setting.enemyY4)),
        screen.blit(Enemy.moveEnemy[random.randint(0, 1)], (setting.enemyX4, setting.enemyY))

    def Crash(self):
        playerRect = setting.PLAYERIMG.get_rect()
        playerRect.left = setting.playerX
        playerRect.top = setting.playerY

        enemyRect = Enemy.moveEnemy[0].get_rect()
        enemyRect.left = setting.enemyX2
        enemyRect.top = setting.enemyY3

        enemyRect2 = Enemy.moveEnemy[0].get_rect()
        enemyRect2.left = setting.enemyX3
        enemyRect2.top = setting.enemyY2

        enemyRect3 = Enemy.moveEnemy[0].get_rect()
        enemyRect3.left = setting.enemyX4
        enemyRect3.top = setting.enemyY4

        enemyRect4 = Enemy.moveEnemy[0].get_rect()
        enemyRect4.left = setting.enemyX2
        enemyRect4.top = setting.enemyY

        enemyRect5 = Enemy.moveEnemy[0].get_rect()
        enemyRect5.left = setting.enemyX3
        enemyRect5.top = setting.enemyY4

        enemyRect6 = Enemy.moveEnemy[0].get_rect()
        enemyRect6.left = setting.enemyX4
        enemyRect6.top = setting.enemyY

        if playerRect.colliderect(enemyRect):
            self.endView()
            self.running = False
            self.wait_for_key()

        if playerRect.colliderect(enemyRect2):
            self.endView()
            self.running = False
            self.wait_for_key()

        if playerRect.colliderect(enemyRect3):
            self.endView()
            self.running = False
            self.wait_for_key()

        if playerRect.colliderect(enemyRect4):
            self.endView()
            self.running = False
            self.wait_for_key()

        if playerRect.colliderect(enemyRect5):
            self.endView()
            self.running = False
            self.wait_for_key()

        if playerRect.colliderect(enemyRect6):
            self.endView()
            self.running = False
            self.wait_for_key()

    # 플레이어 공격
    def attack(self):
        attackLeftRect = setting.ATTACKIMG.get_rect()
        attackLeftRect.left = setting.playerX + 35
        attackLeftRect.top = setting.playerY + 15

        attackRightRect = setting.ATTACKIMG.get_rect()
        attackRightRect.right = setting.playerX - 5
        attackRightRect.top = setting.playerY + 15

        enemyRect = Enemy.moveEnemy[0].get_rect()
        enemyRect.left = setting.enemyX
        enemyRect.top = setting.enemyY

        enemyRect2 = Enemy.moveEnemy[0].get_rect()
        enemyRect2.left = setting.enemyX3
        enemyRect2.top = setting.enemyY2

        enemyRect3 = Enemy.moveEnemy[0].get_rect()
        enemyRect3.left = setting.enemyX4
        enemyRect3.top = setting.enemyY4

        enemyRect4 = Enemy.moveEnemy[0].get_rect()
        enemyRect4.left = setting.enemyX2
        enemyRect4.top = setting.enemyY

        enemyRect5 = Enemy.moveEnemy[0].get_rect()
        enemyRect5.left = setting.enemyX3
        enemyRect5.top = setting.enemyY4

        enemyRect6 = Enemy.moveEnemy[0].get_rect()
        enemyRect6.left = setting.enemyX4
        enemyRect6.top = setting.enemyY

        if attackLeftRect.colliderect(enemyRect):
            print("왼쪽공격")

        if attackRightRect.colliderect(enemyRect):
            print("오른쪽공격")

        if attackLeftRect.colliderect(enemyRect2):
            print("왼쪽공격")

        if attackRightRect.colliderect(enemyRect2):
            print("오른쪽공격")

        if attackLeftRect.colliderect(enemyRect3):
            print("왼쪽공격")

        if attackRightRect.colliderect(enemyRect3):
            print("오른쪽공격")

        if attackLeftRect.colliderect(enemyRect4):
            print("왼쪽공격")

        if attackRightRect.colliderect(enemyRect4):
            print("오른쪽공격")

        if attackLeftRect.colliderect(enemyRect5):
            print("왼쪽공격")

        if attackRightRect.colliderect(enemyRect5):
            print("오른쪽공격")

        if attackLeftRect.colliderect(enemyRect6):
            print("왼쪽공격")

        if attackRightRect.colliderect(enemyRect6):
            print("오른쪽공격")
game = MAIN()

game.startView()
while game.running :
    game.mainGame()
    game.Crash()
    pg.display.update()
game.endView()