from cell import Cell

class Entropy:

    def get_entropy_score(self, grid, index):
        pass

    def collapse(self, grid, index):
        pass

    def is_start(self, grid):
        return all(all(isinstance(x, Cell) for x in row) for row in grid)
