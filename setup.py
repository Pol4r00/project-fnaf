import pygame

SCREEN_WIDTH = 980
SCREEN_HEIGHT = 680

Q1 = pygame.Rect(0, 0, round(SCREEN_WIDTH / 3), SCREEN_HEIGHT)
Q2 = pygame.Rect(SCREEN_WIDTH - round(SCREEN_WIDTH / 3), 0, round(SCREEN_WIDTH / 3), SCREEN_HEIGHT)
Q3 = pygame.Rect(Q1.width * 0.75, SCREEN_HEIGHT * 0.9, SCREEN_WIDTH - Q1.width - Q2.width + (Q1.width * 0.5), SCREEN_HEIGHT * 0.1)

CAPTION = "project-fnaf"
ICON = "assets/foxy.png"

FRAMERATE_CAP = 60
PLAYER_VEL = 18
ENEMY_VEL = 5000

DEFAULT_COLOR = (255, 10, 120)


