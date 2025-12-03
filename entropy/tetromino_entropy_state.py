from typing import TypedDict


class TetrominoEntropy(TypedDict):
    score: int
    isCollapsed: bool

class TetrominoEntropyState(TypedDict):
    top: TetrominoEntropy 
    left: TetrominoEntropy
    right: TetrominoEntropy
    bottom: TetrominoEntropy

