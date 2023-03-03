import random
import time
from itertools import cycle
import pygame
from pygame.constants import QUIT

pygame.init()
screen = width, height = 1200, 800
BLACK = 0, 0, 0
COLOR = ((255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 255, 255), (0, 255, 255))
cycle_iter_color = cycle(COLOR)
main_surface = pygame.display.set_mode(screen)

# Load image
ball_image = pygame.image.load("ball.png")
ball_rect = ball_image.get_rect()
ball_pos = [width//2, height//2]
ball_speed = [1, 1]

is_working = True
while is_working:
    time.sleep(0.002)
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    if ball_pos[1] + ball_rect.height >= height or ball_pos[1] <= 0:
        ball_speed[1] = -ball_speed[1]
        # ball_image.fill(next(cycle_iter_color))

    if ball_pos[0] + ball_rect.width >= width or ball_pos[0] <= 0:
        ball_speed[0] = -ball_speed[0]
        # ball_image.fill(next(cycle_iter_color))

    main_surface.fill(BLACK)
    main_surface.blit(ball_image, ball_pos)
    pygame.display.flip()
