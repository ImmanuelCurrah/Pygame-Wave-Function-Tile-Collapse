from .tetromino import Tetromino
import pygame

class LeftLateralTetromino(Tetromino):

    def __init__(self, cell_size):
        self.cell_size = cell_size
        self.bar_thickness = cell_size // 3
        self.surface = pygame.Surface((self.cell_size, self.cell_size), pygame.SRCALPHA)

    def draw_tetromino(self, screen: pygame.Surface, x: int, y: int):
        mid = self.cell_size // 2
        half_t = self.bar_thickness // 2

       # pygame.draw.rect(self.surface, self.color,(0, mid - half_t, mid - half_t, self.bar_thickness))
        #pygame.draw.rect(self.surface, self.color, (mid - half_t, 0, self.bar_thickness, self.cell_size))
        #creen.blit(self.surface, (x, y))

       
        #pygame.draw.rect(self.surface, self.color, (mid, 0, self.cell_size, self.bar_thickness))
        #pygame.draw.rect(self.surface, self.color, (mid - half_t, 0, mid - half_t, self.cell_size))
        #pygame.draw.rect(self.surface, self.color, (0, 0, self.bar_thickness, self.cell_size)) 

        # horizontal right bar
        pygame.draw.rect(self.surface, self.color, (mid, mid - half_t, mid, self.bar_thickness))
        # vertical left bar
        pygame.draw.rect(self.surface, self.color, (mid - half_t, 0, self.bar_thickness, self.cell_size))
        screen.blit(self.surface, (x, y))
