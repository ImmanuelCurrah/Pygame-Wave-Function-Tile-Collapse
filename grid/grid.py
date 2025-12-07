import pygame
from cell import Cell

class Grid:

    grid = []
    cell_size = 0

    def __init__(self, rows, cols, cell_size):
        self.grid = [[Cell() for _ in range(cols)] for _ in range(rows)]
        self.cell_size = cell_size

    def draw_grid(self, screen):

        for row_index, rows in enumerate(self.grid):
            for col_index, cell in enumerate(rows):
                 x = col_index * self.cell_size
                 y = row_index * self.cell_size

                 cell.draw_cell(screen, x, y, self.cell_size)

