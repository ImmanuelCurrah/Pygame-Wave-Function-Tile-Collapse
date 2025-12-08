from abc import ABC, abstractmethod
import pygame

class Tetromino(ABC):

    surface: pygame.Surface
    cell_size: int
    bar_thickness: int

    color = "purple"

    @abstractmethod
    def draw_tetromino(self, screen: pygame.Surface, x: int, y: int) -> None:
        pass    
