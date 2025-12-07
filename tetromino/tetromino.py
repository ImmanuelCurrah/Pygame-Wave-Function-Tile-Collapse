from abc import ABC, abstractmethod
import pygame

class Tetromino(ABC):

    surface: pygame.Surface
    x: int
    y: int

    cell_size = 10
    tile_size = cell_size * 3
    color = "purple"

    @abstractmethod
    def draw_tetromino(self, screen: pygame.Surface, x: int, y: int) -> None:
        pass    

    def get_rect(self) -> pygame.Rect:
        return self.surface.get_rect(topleft=(self.x, self.y))
