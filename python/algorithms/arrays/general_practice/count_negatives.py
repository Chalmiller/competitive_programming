from typing import *

def countNegatives(grid: List[List[int]]) -> int:
    return(len([item for sublist in grid for item in sublist if item < 0]))