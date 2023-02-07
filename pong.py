import pygame
import sys

pygame.init()
clock = pygame.time.Clock()

# SETTINGS
FPS = 60
BACKGROUND_COLOR = pygame.Color('grey12')
SCREEN_WIDTH = 1024
SCREEN_HEIGHT = 768
SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption('Pong')

BALL = pygame.Rect(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2 - 15, 30, 30)
PLAYER = pygame.Rect(SCREEN_WIDTH - 20, SCREEN_HEIGHT / 2 - 70, 10, 140)
OPPONENT = pygame.Rect(10, SCREEN_HEIGHT / 2 - 70, 10, 140)

# MAIN LOOP
while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    SCREEN.fill(BACKGROUND_COLOR)

    # DRAW ELEMENTS
    ELEMENTS_COLOR = (200, 200, 200)
    pygame.draw.rect(SCREEN, ELEMENTS_COLOR, PLAYER)
    pygame.draw.rect(SCREEN, ELEMENTS_COLOR, OPPONENT)
    pygame.draw.ellipse(SCREEN, ELEMENTS_COLOR, BALL)
    pygame.draw.aaline(SCREEN, ELEMENTS_COLOR, (SCREEN_WIDTH / 2, 0), (SCREEN_WIDTH / 2, SCREEN_HEIGHT))

    pygame.display.flip()
    clock.tick(FPS)
