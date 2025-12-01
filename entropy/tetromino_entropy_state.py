from typing import TypedDict

class TetrominoEntropyState(TypedDict):
    top: bool 
    left: bool
    right: bool
    bottom: bool

