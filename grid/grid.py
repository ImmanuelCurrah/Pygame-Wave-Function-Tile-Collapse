import pygame
import math
import random
from cell import Cell
from entropy import Entropy

class Grid:

    grid = []
    cell_size = 0
    entropy = Entropy()
    random_start = {}

    start_tetromino = random.choice(["Upright Tetromino", "Upside Down Tetromino", "Right Lateral Tetromino", "Left Lateral Tetromino"])

    def __init__(self, screen_width, screen_height):
        self.cell_size = math.gcd(screen_width, screen_height)
        self.grid = [[Cell("Blank Cell") for _ in range(screen_width // self.cell_size)] for _ in range(screen_height // self.cell_size)]
        self.random_start["row_index"] = random.randint(0, len(self.grid) -1)
        self.random_start["col_index"] = random.randint(0, len(self.grid[self.random_start["row_index"]]) - 1)

    def collapse(self, screen):
        lowest_entropy_cell = self.entropy.get_entropy_summary(self.grid)

        for row, rows in enumerate(self.grid):
            for col, cell in enumerate(rows):
                x = col * self.cell_size
                y = row * self.cell_size

                if self.entropy.is_start(self.grid) and row == self.random_start["row_index"] and col == self.random_start["col_index"]:
                    self.grid[row][col] = Cell(self.start_tetromino, True)
                elif len(lowest_entropy_cell) > 0:
                    tetromino = "Blank Cell" if len(lowest_entropy_cell["options"]) == 1 else random.choice([opt for opt in lowest_entropy_cell["options"] if opt != "Blank Cell"])
                    self.grid[lowest_entropy_cell["coords"][0]][lowest_entropy_cell["coords"][1]] = Cell(tetromino, True)

                cell.draw_cell(screen, x, y, self.cell_size)
    
