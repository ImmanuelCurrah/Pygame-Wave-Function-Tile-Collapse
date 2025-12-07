import pygame

class Grid:

    def __init__(self):
        pass

    def draw_grid(self, screen, rows, cols, cell_size):
        for row in range(rows):
            for col in range(cols):
                 x = col * cell_size
                 y = row * cell_size
                 rect = pygame.Rect(x, y, cell_size, cell_size)
                 pygame.draw.rect(screen, "black", rect, width=1)

