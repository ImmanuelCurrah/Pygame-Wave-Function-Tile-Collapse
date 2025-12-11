from .tetromino import Tetromino
import pygame

class UprightTetromino(Tetromino):

    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.bar_thickness = cell_size // 3
        self.surface = pygame.Surface((self.cell_size, self.cell_size), pygame.SRCALPHA)

    def draw_tetromino(self, screen: pygame.Surface, x: int, y: int) -> None:
        mid = self.cell_size // 2
        half_t = self.bar_thickness // 2

        pygame.draw.rect(self.surface, self.color, (0, mid - half_t, self.cell_size, self.bar_thickness))
        pygame.draw.rect(self.surface, self.color, (mid - half_t, mid, self.bar_thickness, self.cell_size - mid))
        screen.blit(self.surface, (x, y))
