# Color Setting
import pygame.mixer

# Color Setting
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
WHITE = (255, 255, 255)

# Game Setting
size = [1500, 850]
HALF_WIDTH = size[0] // 2
HALF_HEIGHT = size[1] // 2

# Font Setting
font_name = 'DEMON_NI.ttf'

# text
TITLE = "OVERROAD"

# mapImage
MAPIMG = pygame.image.load("mapIMG.png")
MAPIMG = pygame.transform.scale(MAPIMG, (1600, 1600))

# sound
pygame.init()
BGM = pygame.mixer.Sound("bgm.mp3")

# player
PLAYERIMG = pygame.image.load("user1.png")
PLAYERLEFTIMG = pygame.image.load("user1Left.png")
PLAYERIMG = pygame.transform.scale(PLAYERIMG, (30, 55))
PLAYERLEFTIMG = pygame.transform.scale(PLAYERIMG, (30, 55))
playerX = 720
playerY = 400
ATTACKIMG = pygame.image.load("attack.png")

# enemy
enemyX = 600
enemyY = 700
