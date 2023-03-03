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

ball = pygame.Surface((100, 100))
ball.fill(WHITE)
ball_rect = ball.get_rect()
ball_speed = [1, 1]

is_working = True
while is_working:
    time.sleep(0.002)
    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

    ball_rect = ball_rect.move(ball_speed)
    if ball_rect.bottom >= height or ball_rect.top <= 0:
        ball_speed[1] = -ball_speed[1]
        ball.fill(next(cycle_iter_color))

    if ball_rect.left >= width-100 or ball_rect.right-100 <= 0:
        ball_speed[0] = -ball_speed[0]
        ball.fill(next(cycle_iter_color))

    main_surface.fill(BLACK)
    main_surface.blit(ball, ball_rect)
    # main_surface.fill((155, 155, 155))
    pygame.display.flip()
