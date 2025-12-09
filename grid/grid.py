import pygame
import math
import random
from cell import Cell
from entropy import Entropy

class Grid:

    grid = []

    cell_size = 0

    entropy: Entropy

    random_start = {}

    start_tetromino = random.choice(["Upright Tetromino", "Upside Down Tetromino", "Right Lateral Tetromino", "Left Lateral Tetromino"])

    def __init__(self, screen_width, screen_height):
        self.cell_size = math.gcd(screen_width, screen_height)

        self.grid = [[Cell() for _ in range(screen_width // self.cell_size)] for _ in range(screen_height // self.cell_size)]

        row_index, col_index = self.__get_random_grid_index()
        self.random_start["row_index"] = row_index
        self.random_start["col_index"] = col_index
        self.entropy = Entropy(self.grid)

    def draw_grid(self, screen):
        is_start = self.entropy.is_start(self.grid)
        start_coords, end_coords = self.entropy.get_start_end_coords()

        for current_row_index, rows in enumerate(self.grid):
            for current_col_index, cell in enumerate(rows):
                x = current_col_index * self.cell_size
                y = current_row_index * self.cell_size

                if (current_row_index, current_col_index) in set(start_coords):
                   cell.draw_cell(screen, x, y, self.cell_size, self.start_tetromino)
                elif (current_col_index, current_row_index) in set(end_coords):
                    cell.draw_cell(screen, x, y, self.cell_size, self.start_tetromino)
                elif is_start and current_row_index == self.random_start["row_index"] and current_col_index == self.random_start["col_index"]:
                    cell.draw_cell(screen, x, y, self.cell_size, self.start_tetromino)
                else:
                    cell.draw_cell(screen, x, y, self.cell_size, "Blank Cell")

    def __get_random_grid_index(self):
        row_index = random.randint(0, len(self.grid) -1)
        col_index = random.randint(0, len(self.grid[row_index]) - 1)

        return row_index, col_index
    
