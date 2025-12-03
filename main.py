import pygame
import random

from tetromino import Tetromino, UprightTetromino, UpsideDownTetromino, RightLateralTetromino, LeftLateralTetromino

pygame.init()

screen = pygame.display.set_mode((1280, 720))
running = True

start_x_pos = random.randint(10, 500)
start_y_pos = random.randint(10, 500)

def draw_grid(screen, rows, cols, cell_size):
    for row in range(rows):
        for col in range(cols):
            x = col * cell_size
            y = row * cell_size

            if row == 5 and col == 5:
                UprightTetromino().draw_tetromino(screen, x, y)
            else:
                rect = pygame.Rect(x, y, cell_size, cell_size)
                pygame.draw.rect(screen, "black", rect, width=1)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    screen.fill("black")

    draw_grid(screen, 10, 10, 10 * 3)


    pygame.display.flip()
    pygame.time.Clock().tick(60)


pygame.quit()
