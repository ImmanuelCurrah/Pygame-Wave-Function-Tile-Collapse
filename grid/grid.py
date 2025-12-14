import pygame
import math
import random
from cell import Cell
from entropy import Entropy

class Grid:

    grid = []
    cell_size = 0
    entropy = Entropy()
    start_tetromino = random.choice(["Upright Tetromino", "Upside Down Tetromino", "Right Lateral Tetromino", "Left Lateral Tetromino"])

    def __init__(self, screen_width, screen_height):
        self.cell_size = 25
        self.grid = [[Cell("Blank Cell", False) for _ in range(screen_width // self.cell_size)] for _ in range(screen_height // self.cell_size)]
        self.grid[random.randrange(len(self.grid))][random.randrange(len(self.grid[0]))] = Cell(self.start_tetromino, True)

    def collapse(self, screen):
        lowest = self.entropy.get_lowest_entropy(self.grid)

        for row, rows in enumerate(self.grid):
            for col, cell in enumerate(rows):
                x = col * self.cell_size
                y = row * self.cell_size
               
                if lowest != None:
                    tetromino = "Blank Cell" if len(lowest["options"]) == 1 else random.choice([opt for opt in lowest["options"] if opt != "Blank Cell"]) 
                    self.grid[lowest["coords"][0]][lowest["coords"][1]] = Cell(tetromino, True)
                    
                cell.draw_cell(screen, x, y, self.cell_size) 
