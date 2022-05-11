import pygame as pg
import random
import setting

class Enemy :
    moveEnemy = [pg.image.load('enemy1.png'), pg.image.load('enemy2.png')]
    moveEnemy = pg.transform.scale(moveEnemy[0], (55, 50)), pg.transform.scale(moveEnemy[1], (55, 50))

    def __init__(self, name, enemyX, enemyY):
        self.name = name
        self.enemyX = enemyX
        self.enemyY = enemyY


    def enemyMove(self):
        maxX = 1410
        maxY = 760
        minX = 10
        minY = 10

        if self.enemyX >= maxX :
            self.enemyX = random.randint(10, 1400)
        elif self.enemyX <= minX :
            self.enemyX = random.randint(10, 1400)
        # if setting.enemyX2 >= maxX :
        #     setting.enemyX2 = random.randint(10, 1400)
        # elif setting.enemyX2 <= minX :
        #     setting.enemyX2 = random.randint(10, 1400)
        # if setting.enemyX3 >= maxX :
        #     setting.enemyX3 = random.randint(10, 1400)
        # elif setting.enemyX3 <= minX :
        #     setting.enemyX3 = random.randint(10, 1400)
        # if setting.enemyX4 >= maxX :
        #     setting.enemyX4 = random.randint(10, 1400)
        # elif setting.enemyX4 <= minX :
        #     setting.enemyX4 = random.randint(10, 1400)
        # if setting.enemyY >= maxY :
        #     setting.enemyY = random.randint(10, 750)
        # elif setting.enemyY <= minY :
        #     setting.enemyY = random.randint(10, 750)
        # if setting.enemyY2 >= maxY :
        #     setting.enemyY2 = random.randint(10, 750)
        # elif setting.enemyY2 <= minY :
        #     setting.enemyY2 = random.randint(10, 750)
        # if setting.enemyY3 >= maxY :
        #     setting.enemyY3 = random.randint(10, 750)
        # elif setting.enemyY3 <= minY :
        #     setting.enemyY3 = random.randint(10, 750)
        # if setting.enemyY4 >= maxY :
        #     setting.enemyY4 = random.randint(10, 750)
        # elif setting.enemyY <= minY :
        #     setting.enemyY = random.randint(10, 750)

        setting.enemyX += 0.35
        setting.enemyX2 -= 0.35
        setting.enemyX3 += 0.35
        setting.enemyX4 -= 0.35
        setting.enemyY += 0.35
        setting.enemyY2 += 0.35
        setting.enemyY3 -= 0.35
        setting.enemyY4 += 0.35


        # enemy1 = screen.blit(Enemy.moveEnemy[0], (setting.enemyX, setting.enemyY)),
        # screen.blit(Enemy.moveEnemy[random.randint(0, 1)], (setting.enemyX2, setting.enemyY3)),
        # screen.blit(Enemy.moveEnemy[random.randint(0, 1)], (setting.enemyX3, setting.enemyY2)),
        # screen.blit(Enemy.moveEnemy[random.randint(0, 1)], (setting.enemyX4, setting.enemyY4)),
        # screen.blit(Enemy.moveEnemy[random.randint(0, 1)], (setting.enemyX2, setting.enemyY)),
        # screen.blit(Enemy.moveEnemy[random.randint(0, 1)], (setting.enemyX3, setting.enemyY4)),
        # screen.blit(Enemy.moveEnemy[random.randint(0, 1)], (setting.enemyX4, setting.enemyY))
