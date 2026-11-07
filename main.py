import pygame

pygame.font.init()
pygame.mixer.init()

WIDTH = 900
HEIGHT = 500
CENTER_X = WIDTH // 2
CENTER_Y = HEIGHT // 2
CENTER = (CENTER_X,CENTER_Y)

SCREEN = pygame.display.set_mode(('bg.png'))
pygame.display.set_caption('Ship Duels')
BORDER = pygame.Rect(445 , 0 , 10, HEIGHT )

BULLET_HIT_SOUND = pygame.mixer.Sound('Grenade+1.mp3')
BULLET_FIRE_SOUND = pygame.mixer.Sound('Gun+Silencer.mp3')

HEALTH_FONT = pygame.font.SysFont('comicsans', 35)
WINNER_FONT = pygame.font.Sysfont('comicsans', 100)

FPS = 60
VEL = 5
BULLET_VEL = 7
MAX_BULLETS = 3
SPACESHIP_WIDTH = 55
SPACESHIP_HEIGHT = 40

YELLOW_SPACESHIP_IMG = pygame.image.load('yellow_ship.png')
YELLOW_SPACESHIP = pygame.transform.rotate(pygame.transform.scale(YELLOW_SPACESHIP_IMG,(SPACESHIP_WIDTH, SPACESHIP_HEIGHT)))

RED_SPACESHIP_IMG = pygame.image.load('red_ship.png')
RED_SPACESHIP = pygame.transform.rotate (pygame.transform.scale (RED_SPACESHIP_IMG (SPACESHIP_WIDTH, SPACESHIP_HEIGHT)))

SPACE_IMG = pygame.image.load('bg.png')
SPACE = pygame.transform.scale(SPACE_IMG, (WIDTH, HEIGHT))
