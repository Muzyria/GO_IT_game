import random
import pygame
from pygame.constants import QUIT, K_DOWN, K_UP, K_LEFT, K_RIGHT
from os import listdir
from itertools import cycle

pygame.init()

FPS = pygame.time.Clock()

screen = width, height = 1200, 700

BLACK = 0, 0, 0
WHITE = 255, 255, 255
RED = 255, 0, 0
GREEN = 0, 255, 0

IMGS_PATH = "img/player_img"

font = pygame.font.SysFont("Verdana", 20)

main_surface = pygame.display.set_mode(screen)

# player_img = [pygame.image.load(f'{IMGS_PATH}/{file}').convert_alpha() for file in listdir(IMGS_PATH)]
# player_iter_img_cycle = cycle(player_img)
# player = next(player_iter_img_cycle)
player = pygame.image.load("img/player_2.png").convert_alpha()
player_rect = player.get_rect()
player_speed = 5

enemy_img = pygame.image.load("img/enemy_2.png").convert_alpha()
bonus_img = pygame.image.load("img/bonus_2.png").convert_alpha()


def create_enemy():
    # enemy_create = pygame.transform.scale(enemy_img, (enemy_img.get_width() / 2, enemy_img.get_height() / 2))
    enemy_create = enemy_img
    enemy_rect = pygame.Rect(width, random.randint(0, height - enemy_img.get_height()), *enemy_create.get_size())
    enemy_speed = random.randint(2, 5)
    return [enemy_create, enemy_rect, enemy_speed]


def create_bonus():
    # bonus_create = pygame.transform.scale(bonus_img, (bonus_img.get_width()/2, bonus_img.get_height()/2))
    bonus_create = bonus_img
    bonus_rect = pygame.Rect(random.randint(0, width - bonus_img.get_width()), -bonus_create.get_height(), *bonus_create.get_size())
    bonus_speed = random.randint(2, 5)
    return [bonus_create, bonus_rect, bonus_speed]


bg = pygame.transform.scale(pygame.image.load("img/background.png").convert(), screen)
bgx = 0
bgx2 = bg.get_width()
bg_speed = 3

CREATE_ENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(CREATE_ENEMY, 1500)
CREATE_BONUS = pygame.USEREVENT + 2
pygame.time.set_timer(CREATE_BONUS, 2500)
CHANGE_IMG = pygame.USEREVENT + 3
pygame.time.set_timer(CHANGE_IMG, 125)

img_index = 0

scores = 0

bonuses = []
enemies = []

is_working = True
while is_working:

    FPS.tick(60)

    for event in pygame.event.get():
        if event.type == QUIT:
            is_working = False

        if event.type == CREATE_ENEMY:
            enemies.append(create_enemy())

        if event.type == CREATE_BONUS:
            bonuses.append(create_bonus())

        # if event.type == CHANGE_IMG:
        #     player = next(player_iter_img_cycle)

    pressed_keys = pygame.key.get_pressed()

    bgx -= bg_speed
    bgx2 -= bg_speed
    if bgx < -bg.get_width():
        bgx = bg.get_width()
    if bgx2 < -bg.get_width():
        bgx2 = bg.get_width()
    main_surface.blit(bg, (bgx, 0))
    main_surface.blit(bg, (bgx2, 0))

    main_surface.blit(player, player_rect)
    main_surface.blit(font.render(str(scores), True, BLACK), (width - 30, 0))

    for enemy in enemies:
        enemy[1] = enemy[1].move(-enemy[2], 0)
        main_surface.blit(enemy[0], enemy[1])
        if enemy[1].left < -bonus_img.get_width():
            enemies.remove(enemy)
        if player_rect.colliderect(enemy[1]):
            is_working = False

    for bonus in bonuses:
        bonus[1] = bonus[1].move(0, bonus[2])
        main_surface.blit(bonus[0], bonus[1])
        if bonus[1].bottom > height + bonus_img.get_height():
            bonuses.remove(bonus)
        if player_rect.colliderect(bonus[1]):
            bonuses.remove(bonus)
            scores += 1

    if pressed_keys[K_DOWN] and not player_rect.bottom >= height:
        player_rect = player_rect.move((0, player_speed))
    if pressed_keys[K_UP] and not player_rect.top <= 0:
        player_rect = player_rect.move((0, -player_speed))
    if pressed_keys[K_RIGHT] and not player_rect.right >= width:
        player_rect = player_rect.move((player_speed, 0))
    if pressed_keys[K_LEFT] and not player_rect.left <= 0:
        player_rect = player_rect.move((-player_speed, 0))

    # main_surface.fill((155, 155, 155))
    pygame.display.flip()
