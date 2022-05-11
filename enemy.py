import pygame as pg
import random
import setting
import main

class Enemy :
    moveEnemy = (pg.image.load('enemy1.png'), pg.image.load('enemy2.png'))
    moveList = list(moveEnemy)
    moveEnemy = pg.transform.scale(moveEnemy[0], (55, 50)), pg.transform.scale(moveEnemy[1], (55, 50))
    hmm = True

    def __init__(self, name):
        self.name = name

    # 플레이어 공격
    def attack(self):
            attackLeftRect = setting.ATTACKIMG.get_rect()
            attackLeftRect.left = setting.playerX + 35
            attackLeftRect.top = setting.playerY + 15

            attackRightRect = setting.ATTACKIMG.get_rect()
            attackRightRect.right = setting.playerX - 5
            attackRightRect.top = setting.playerY + 15

            enemyRect = self.moveEnemy[0].get_rect()
            enemyRect.left = setting.enemyX
            enemyRect.top = setting.enemyY

            if attackLeftRect.colliderect(enemyRect):
                self.hmm = False
                if self.hmm == False :
                    main.screen.blit(self.moveEnemy[0], (setting.deadEnemy, setting.deadEnemy))
                    pg.display.update()
                    print("왼쪽공격")

            if attackRightRect.colliderect(enemyRect):
                main.screen.blit(self.moveEnemy[0], (setting.deadEnemy, setting.deadEnemy))
                pg.display.update()
                print("오른쪽공격")

    def enemyMove(self):

        if self.hmm == True :
            maxX = 1410
            maxY = 760
            minX = 10
            minY = 10

            if setting.enemyX >= maxX:
                setting.enemyX = random.randint(10, 1400)
            elif setting.enemyX <= minX:
                setting.enemyX = random.randint(10, 1400)

            if setting.enemyY >= maxY:
                setting.enemyY = random.randint(10, 750)
            elif setting.enemyY <= minY:
                setting.enemyY = random.randint(10, 750)

            setting.enemyX += 0.35
            setting.enemyY += 0.35

            main.screen.blit(self.moveEnemy[0], (setting.enemyX, setting.enemyY))
        else :
            print("잡았다!")
            main.screen.blit(self.moveEnemy[0], (setting.deadEnemy, setting.deadEnemy))
            pg.display.update()