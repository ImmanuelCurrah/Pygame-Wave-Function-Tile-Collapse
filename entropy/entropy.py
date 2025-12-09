import math
from cell import Cell

class Entropy:
    
    cols: int

    def __init__(self, grid):
        self.cols = len(grid[0])
    
    def get_start_end_coords(self):
        start_indices = []
        end_indices = []

        start_coords = []
        end_coords = []

        for index in range(self.cols):
            start_index = index * (self.cols - 1)
            end_index = start_index + (self.cols - 1)
            start_indices.append(start_index)
            end_indices.append(end_index)

            start_coords.append((index, 0))
            end_coords.append((self.cols - 1, index))

        return start_coords, end_coords




    def get_entropy_score(self):
        pass

    def is_start(self, grid):
        return all(all(isinstance(x, Cell) for x in row) for row in grid)
