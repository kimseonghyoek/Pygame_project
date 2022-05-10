import pygame as pg
import random
import setting

class Enemy :
    def __init__(self, name):
        self.name = name
    moveEnemy = [pg.image.load('enemy1.png'), pg.image.load('enemy2.png')]
    moveEnemy = pg.transform.scale(moveEnemy[0], (55, 50)), pg.transform.scale(moveEnemy[1], (55, 50))

