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
MAPIMG = pygame.transform.scale(MAPIMG, (1800, 1800))

# sound
pygame.init()
BGM = pygame.mixer.Sound("bgm.mp3")

# player
PLAYERIMG = pygame.image.load("player.png")
PLAYERIMG = pygame.transform.scale(PLAYERIMG, (40, 95))
playerX = 800
playerY = 300
playerSpeed = 5