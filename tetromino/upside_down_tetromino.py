from .tetromino import Tetromino
import pygame


class  UpsideDownTetromino(Tetromino):

    def __init__(self):
        self.surface = pygame.Surface((self.tile_size, self.tile_size), pygame.SRCALPHA)
        self.x = 0
        self.y = 0


    def draw_tetromino(self, screen: pygame.Surface, x: int, y: int) -> None:
        self.x = x
        self.y = y
        pygame.draw.rect(self.surface, self.color, (0, 2 * self.cell_size, self.tile_size, self.cell_size))  
        pygame.draw.rect(self.surface, self.color, (self.cell_size, 0, self.cell_size, self.tile_size))
        screen.blit(self.surface, self.get_rect())
