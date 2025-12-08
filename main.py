import pygame
from window import Window
from grid import Grid

pygame.init()

screen_width = 1280
screen_height = 720
screen = pygame.display.set_mode((screen_width, screen_height))

window = Window()
grid = Grid(screen_width, screen_height)

while window.showWindow:
    window.handleWindow(pygame.event.get())

    screen.fill("white")

    grid.draw_grid(screen)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
