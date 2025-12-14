import math
import random
from cell import Cell

class Entropy:

    def get_lowest_entropy(self, grid):        
        entropy_summary = []

        for row, row_cells in enumerate(grid):
            for col, cell in enumerate(row_cells):
                if cell.is_collapsed == False:
                    current_cell_entropy_score = 0
                    current_top_options = []
                    current_bottom_options = []
                    current_right_options = []
                    current_left_options = []
                    all_options = [current_top_options, current_bottom_options, current_right_options, current_left_options]

                    blank = "Blank Cell"
                    t = "Upright Tetromino"
                    b = "Upside Down Tetromino"
                    r = "Right Lateral Tetromino"
                    l = "Left Lateral Tetromino"

                    top = grid[row - 1][col].cell_type if row > 0 else None
                    bottom = grid[row + 1][col].cell_type if row + 1 < len(grid) else None
                    right = grid[row][col + 1].cell_type if col + 1 < len(row_cells) else None
                    left = grid[row][col - 1].cell_type if col > 0 else None

                    if top == "Blank Cell":
                        current_top_options.extend([t, b, r, l, blank])
                    elif top == t:
                        current_top_options.extend([b, r, l, blank])
                    elif top == b:
                        current_top_options.extend([t, blank])
                    elif top == r:
                        current_top_options.extend([b, r, l, blank])
                    elif top == l:
                        current_top_options.extend([b, r, l, blank])

                    if bottom == "Blank Cell":
                        current_bottom_options.extend([t, b, r, l, blank])
                    elif bottom == t: 
                        current_bottom_options.extend([b, blank])
                    elif bottom == b:
                        current_bottom_options.extend([t, r, l, blank])
                    elif bottom == r:
                        current_bottom_options.extend([r, l, t, blank])
                    elif bottom == l:
                        current_bottom_options.extend([r, l, t, blank])

                    if right == "Blank Cell":
                        current_right_options.extend([t, b, r, l, blank])
                    elif right == t:
                        current_right_options.extend([t, l, b, blank])
                    elif right == b:
                        current_right_options.extend([t, l, b, blank])
                    elif right == r:
                        current_right_options.extend([l, b, t, blank])
                    elif right == l:
                        current_right_options.extend([r, blank])

                    if left == "Blank Tile":
                        current_left_options.extend([t, b, r, l, blank])
                    elif left == t:
                        current_left_options.extend([b, r, t, blank])
                    elif left == b: 
                        current_left_options.extend([b, t, r, blank])
                    elif left == r: 
                        current_left_options.extend([l, blank])
                    elif left == l:
                        current_left_options.extend([b, t, r, blank])

                    total_options = [blank] if all(not arr for arr in all_options) else list(set.intersection(*(set(lst) for lst in all_options if lst)))
                    entropy_summary.append({"score": len(total_options), "coords": (row, col), "options": total_options})

        lowest_matches = [cell for cell in entropy_summary if cell["score"] == min((cell["score"] for cell in entropy_summary), default=0)]
        return lowest_matches[0] if len(lowest_matches) == 1 else (random.choice(lowest_matches) if len(lowest_matches) > 1 else None)
