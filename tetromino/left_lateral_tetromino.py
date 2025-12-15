from .tetromino import Tetromino
import pygame

class LeftLateralTetromino(Tetromino):

    def __init__(self, cell_size):
        super().__init__(cell_size)

    def draw_tetromino(self, screen: pygame.Surface, x: int, y: int):
        mid = self.cell_size // 2
        half_t = self.bar_thickness // 2


        pygame.draw.rect(self.surface, self.color, (self.bar_thickness * 2, mid - half_t, mid, self.bar_thickness))
        pygame.draw.rect(self.surface, self.color, (mid - half_t, 0, self.bar_thickness, self.cell_size))
        screen.blit(self.surface, (x, y))
