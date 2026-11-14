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

def draw_window(red, yellow, red_bullets, yellow_bullets, red_lives, yellow_lives):
    SCREEN.blit(SPACE, (0,0))
    pygame.draw.rect(SCREEN, 'black', BORDER)

    red_lives_text = HEALTH_FONT.render(f'Health: {red_lives}', 1, 'White')
    SCREEN.blit(red_lives_text, (650,10))

    yellow_lives_text = HEALTH_FONT.render(f'Health: {yellow_lives}', 1, 'White')
    SCREEN.blit(yellow_lives_text, (10,10))


    for bullet in yellow_bullets:
        pygame.draw.rect(SCREEN, 'yellow', bullet)

    for bullet in red_bullets:
        pygame.draw.rect(SCREEN, 'red', bullet)

    pygame.display.update()

def yellow_handle_movement(keys_pressed, yellow):
    if keys_pressed[pygame.K_a] and yellow.x - VEL > 0:
        yellow.x -= VEL

    if keys_pressed[pygame.K_d] and yellow.x + VEL + yellow.width < BORDER.x:
        yellow.x += VEL

    if keys_pressed[pygame.K_w] and yellow.y - VEL > 0:
        yellow.y -= VEL

    if keys_pressed[pygame.K_s] and yellow.y + VEL + yellow.height < HEIGHT - 15:
        yellow.y += VEL

def red_handle_movement(keys_pressed, red):
    if keys_pressed[pygame.K_UP] and red.y - VEL > 0:
        red.y -= VEL

    if keys_pressed[pygame.K_DOWN] and red.y + VEL + red.height < HEIGHT - 15:
        red.y += VEL

    if keys_pressed[pygame.K_LEFT] and red.x - VEL > BORDER.x + BORDER.width:
        red.x -= VEL

    