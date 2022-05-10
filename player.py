import pygame as pg
import pygame.display
import setting
from enemy import Enemy

class Player :
    pg.init()

    rightWalk = [pg.image.load('user1.png'), pg.image.load('user2.png'), pg.image.load('user3.png'), pg.image.load('user4.png'), pg.image.load('user5.png')]
    rightWalk = pg.transform.scale(rightWalk[0], (30, 55)), pg.transform.scale(rightWalk[1], (30, 55)), pg.transform.scale(rightWalk[2], (30, 55)), \
            pg.transform.scale(rightWalk[3], (30, 55)), pg.transform.scale(rightWalk[4], (30, 55))

    leftWalk = [pg.image.load('user1Left.png'), pg.image.load('user2Left.png'), pg.image.load('user3Left.png'), pg.image.load('user4Left.png'), pg.image.load('user5Left.png')]
    leftWalk = pg.transform.scale(leftWalk[0], (30, 55)), pg.transform.scale(leftWalk[1], (30, 55)), pg.transform.scale(leftWalk[2], (30, 55)), \
            pg.transform.scale(leftWalk[3], (30, 55)), pg.transform.scale(leftWalk[4], (30, 55))

    def playerMoveUP(self):
        setting.playerY -= 0.25
    def playerMoveDOWN(self):
        setting.playerY += 0.25
    def playerMoveLEFT(self):
        setting.playerX -= 0.25
    def playerMoveRIGHT(self):
        setting.playerX += 0.25

    # 플레이어 공격
    def attack(self):
        attackLeftRect = setting.ATTACKIMG.get_rect()
        attackLeftRect.left = setting.playerX + 35
        attackLeftRect.top = setting.playerY + 15

        attackRightRect = setting.ATTACKIMG.get_rect()
        attackRightRect.right = setting.playerX - 85
        attackRightRect.top = setting.playerY + 15

        enemyRect = Enemy.moveEnemy[0].get_rect()
        enemyRect.left = setting.enemyX
        enemyRect.top = setting.enemyY
        
        if attackLeftRect.colliderect(enemyRect):
            print(Enemy.enemyList)

        if attackRightRect.colliderect(enemyRect):
            print(Enemy.enemyList)