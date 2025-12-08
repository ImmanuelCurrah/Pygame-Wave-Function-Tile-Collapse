import pygame

from tetromino import UprightTetromino, UpsideDownTetromino, RightLateralTetromino, LeftLateralTetromino

class Cell:
    
    isCollapsed = False

    def __init__(self):
        pass

    def collapse(self):
        self.isCollapsed = True

    def __draw_blank_cell(self, screen, x, y, cell_size):
        rect = pygame.Rect(x, y, cell_size, cell_size)
        pygame.draw.rect(screen, "black", rect, width=1)


    def draw_cell(self, screen, x, y, cell_size, cell_type):
        if cell_type == "Blank Cell":
            self.__draw_blank_cell(screen, x, y, cell_size)
        elif cell_type == "Upright Tetromino":
            self.collapse()
            UprightTetromino(cell_size).draw_tetromino(screen, x, y)
        elif cell_type == "Upside Down Tetromino":
            self.collapse()
            UpsideDownTetromino(cell_size).draw_tetromino(screen, x, y)
        elif cell_type == "Right Lateral Tetromino":
            self.collapse()
            RightLateralTetromino(cell_size).draw_tetromino(screen, x ,y)
        elif cell_type == "Left Lateral Tetromino":
            self.collapse()
            LeftLateralTetromino(cell_size).draw_tetromino(screen, x, y)
        else:
            self.__draw_blank_cell(screen, x, y, cell_size)

