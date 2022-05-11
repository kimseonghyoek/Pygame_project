import pygame as pg
import random
import setting
import main

class Enemy :
    moveEnemy = [pg.image.load('enemy1.png'), pg.image.load('enemy2.png')]
    moveEnemy = pg.transform.scale(moveEnemy[0], (55, 50)), pg.transform.scale(moveEnemy[1], (55, 50))

    def __init__(self, name):
        self.name = name

    def enemyMove(self):

        maxX = 1410
        maxY = 760
        minX = 10
        minY = 10

        if setting.enemyX >= maxX :
            setting.enemyX = random.randint(10, 1400)
        elif setting.enemyX <= minX :
            setting.enemyX = random.randint(10, 1400)

        if setting.enemyY >= maxY :
            setting.enemyY = random.randint(10, 750)
        elif setting.enemyY <= minY :
            setting.enemyY = random.randint(10, 750)


        setting.enemyX += 0.35
        setting.enemyY += 0.35


        main.screen.blit(self.moveEnemy[0], (setting.enemyX, setting.enemyY))