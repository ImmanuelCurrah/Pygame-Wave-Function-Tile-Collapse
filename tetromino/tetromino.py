from abc import ABC, abstractmethod
import pygame

class Tetromino(ABC):

    surface: pygame.Surface
    cell_size: int
    bar_thickness: int
    color = "purple"

    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.bar_thickness = cell_size // 3
        self.surface = pygame.Surface((self.cell_size, self.cell_size), pygame.SRCALPHA)

    @abstractmethod
    def draw_tetromino(self, screen: pygame.Surface, x: int, y: int) -> None:
        pass    
