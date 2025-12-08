from .tetromino import Tetromino
import pygame

class LeftLateralTetromino(Tetromino):

    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.bar_thickness = cell_size // 3
        self.surface = pygame.Surface((self.cell_size, self.cell_size), pygame.SRCALPHA)

    def draw_tetromino(self, screen: pygame.Surface, x: int, y: int) -> None:
        pygame.draw.rect(self.surface, self.color, (0, (self.cell_size - self.bar_thickness) // 2, self.cell_size, self.bar_thickness))

        pygame.draw.rect(self.surface, self.color, (0, 0, self.bar_thickness, self.cell_size)) 

        screen.blit(self.surface, (x, y))
