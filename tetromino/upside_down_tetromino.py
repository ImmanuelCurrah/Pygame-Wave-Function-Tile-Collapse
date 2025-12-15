from .tetromino import Tetromino
import pygame


class  UpsideDownTetromino(Tetromino):

    def __init__(self, cell_size):
        super().__init__(cell_size)


    def draw_tetromino(self, screen: pygame.Surface, x: int, y: int):
        mid = self.cell_size // 2
        half_t = self.bar_thickness // 2

        pygame.draw.rect(self.surface, self.color, (0, mid - half_t, self.cell_size, self.bar_thickness))
        pygame.draw.rect(self.surface, self.color, (mid - half_t, 0, self.bar_thickness, self.cell_size - mid - half_t))
        screen.blit(self.surface, (x, y))
