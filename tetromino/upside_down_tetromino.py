from .tetromino import Tetromino
from entropy import TetrominoEntropyState
import pygame


class  UpsideDownTetromino(Tetromino):

    neighbors: TetrominoEntropyState

    def __init__(self):
        self.surface = pygame.Surface((self.tile_size, self.tile_size), pygame.SRCALPHA)
        self.x = 0
        self.y = 0
        self.neighbors = {"top": False, "bottom": False, "right": False, "left": False}


    def draw_tetromino(self, screen: pygame.Surface, x: int, y: int) -> None:
        self.x = x
        self.y = y
        pygame.draw.rect(self.surface, self.color, (0, 2 * self.cell_size, self.tile_size, self.cell_size))  
        pygame.draw.rect(self.surface, self.color, (self.cell_size, 0, self.cell_size, self.tile_size))
        screen.blit(self.surface, self.get_rect())

    
    def neighbors(self) -> TetrominoEntropyState:
        return self.neighbors

    def entropy_score(self) -> int:
        return 0
