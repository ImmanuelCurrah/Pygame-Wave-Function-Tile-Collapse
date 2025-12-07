import pygame
import random
from window import Window
from grid import Grid

from tetromino import Tetromino, UprightTetromino, UpsideDownTetromino, RightLateralTetromino, LeftLateralTetromino

pygame.init()

window = Window()
grid = Grid()
screen = pygame.display.set_mode((1280, 1280))

start_x_pos = random.randint(10, 500)
start_y_pos = random.randint(10, 500)

while window.showWindow:
    window.handleWindow(pygame.event.get())

    screen.fill("white")

    grid.draw_grid(screen, 25, 25, 15 * 3)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
