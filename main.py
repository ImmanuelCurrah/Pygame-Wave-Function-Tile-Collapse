import pygame
import random

from tetromino import Tetromino, UprightTetromino, UpsideDownTetromino, RightLateralTetromino, LeftLateralTetromino

pygame.init()

screen = pygame.display.set_mode((1280, 720))
running = True

start_x_pos = random.randint(10, 500)
start_y_pos = random.randint(10, 500)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("black")

    tetromino_upright = UprightTetromino()
    tetromino_upright.draw_tetromino(screen, start_x_pos, start_y_pos)
    rect1 = tetromino_upright.get_rect()


    tetromino_upside_down = UpsideDownTetromino()
    tetromino_upside_down.draw_tetromino(screen, rect1.right, start_y_pos)
    rect2 = tetromino_upside_down.get_rect()

    tetromino_right_lateral = RightLateralTetromino()
    tetromino_right_lateral.draw_tetromino(screen, rect2.right, start_y_pos)
    rect3 = tetromino_right_lateral.get_rect()

    tetromino_left_lateral = LeftLateralTetromino()
    tetromino_left_lateral.draw_tetromino(screen, rect3.right, start_y_pos)
    rect4 = tetromino_left_lateral.get_rect()

    pygame.display.flip()
    pygame.time.Clock().tick(60)


pygame.quit()
