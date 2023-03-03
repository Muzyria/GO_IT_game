import random
import time
from itertools import cycle
import pygame
from pygame.constants import QUIT

pygame.init()
screen = width, height = 1200, 400
BLACK = 0, 0, 0
WHITE = 255, 255, 255
COLOR = ((255, 0, 0), (0, 255, 0), (0, 0, 255), (255, 255, 0), (255, 255, 255), (0, 255, 255))
cycle_iter_color = cycle(COLOR)
main_surface = pygame.display.set_mode(screen)

ball_radius = 50
ball_color = WHITE
ball_pos = [width // 2, height // 2]
ball_speed = [1, 1]

is_working = True
while is_working:
    # time.sleep(0.002)
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    if ball_pos[1] + ball_radius >= height or ball_pos[1] - ball_radius <= 0:
        ball_speed[1] = -ball_speed[1]
        ball_color = next(cycle_iter_color)

    if ball_pos[0] + ball_radius >= width or ball_pos[0] - ball_radius <= 0:
        ball_speed[0] = -ball_speed[0]
        ball_color = next(cycle_iter_color)

    main_surface.fill(BLACK)
    pygame.draw.circle(main_surface, ball_color, ball_pos, ball_radius)
    pygame.display.flip()
