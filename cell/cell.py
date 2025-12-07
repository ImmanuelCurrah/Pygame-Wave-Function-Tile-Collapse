import pygame

class Cell:
    
    isCollapsed = False

    def __init__(self):
        pass

    def collapse(self):
        self.isCollapsed = True


    def draw_cell(self, screen, x, y, cell_size):
         rect = pygame.Rect(x, y, cell_size, cell_size)
         pygame.draw.rect(screen, "black", rect, width=1)
