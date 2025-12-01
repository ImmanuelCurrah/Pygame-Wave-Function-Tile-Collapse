from abc import ABC, abstractmethod
from entropy import TetrominoEntropyState
from typing import Literal
import pygame

class Tetromino(ABC):

    surface: pygame.Surface
    x: int
    y: int

    cell_size = 10
    tile_size = cell_size * 3
    color = "purple"

    @property
    @abstractmethod
    def neighbors(self) -> TetrominoEntropyState:
        pass

    @property
    @abstractmethod
    def entropy_score(self) -> int:
        pass

    @abstractmethod
    def draw_tetromino(self, screen: pygame.Surface, x: int, y: int) -> None:
        pass

    def enroll_neighbor(self, orientation: Literal["top", "bottom", "right", "left"]) -> None:
        if self.neighbors[orientation] == True:
            raise ValueError("already enrolled")
        else:
            self.neighbors[orientation] = True
        

    def get_rect(self) -> pygame.Rect:
        return self.surface.get_rect(topleft=(self.x, self.y))
