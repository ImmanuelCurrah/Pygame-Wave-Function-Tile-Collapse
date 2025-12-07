import pygame
import math
from window import Window
from grid import Grid

pygame.init()

screen_width = 1280
screen_height = 730
screen = pygame.display.set_mode((screen_width, screen_height))

window = Window()
grid = Grid(25, 25, 25)

while window.showWindow:
    window.handleWindow(pygame.event.get())

    screen.fill("white")

    grid.draw_grid(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
