import pygame

from tetromino import UprightTetromino, UpsideDownTetromino, RightLateralTetromino, LeftLateralTetromino

class Cell:
    
    is_collapsed = False
    cell_type: str

    def __init__(self, cell_type, is_collapsed):
        self.cell_type = cell_type
        self.is_collapsed = is_collapsed


    def collapse(self, screen, x, y, cell_size, cell_type):
        self.cell_type = cell_type
        self.draw_cell(screen, x, y, cell_size)

    def draw_blank_cell(self, screen, x, y, cell_size):
        pygame.draw.rect(screen, "black", (x, y, cell_size, cell_size))


    def draw_cell(self, screen, x, y, cell_size):
        if self.cell_type == "Blank Cell":
            self.draw_blank_cell(screen, x, y, cell_size)
        elif self.cell_type == "Upright Tetromino":
            UprightTetromino(cell_size).draw_tetromino(screen, x, y)
        elif self.cell_type == "Upside Down Tetromino":
            UpsideDownTetromino(cell_size).draw_tetromino(screen, x, y)
        elif self.cell_type == "Right Lateral Tetromino":
            RightLateralTetromino(cell_size).draw_tetromino(screen, x ,y)
        elif self.cell_type == "Left Lateral Tetromino":
            LeftLateralTetromino(cell_size).draw_tetromino(screen, x, y)
        else:
            self.draw_blank_cell(screen, x, y, cell_size)

