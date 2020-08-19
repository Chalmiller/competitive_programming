from typing import *
import unittest

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        # Global variable assignment
        self.ROWS = len(grid) - 1
        self.COLS = len(grid[0]) - 1

        def consume(row, col, grid):
            if row < 0 or row > self.ROWS or col < 0 or col > self.COLS  or grid[row][col] == '0':
                return grid
            else:
                grid[row][col] = '0'
                consume(row+1, col, grid); consume(row-1, col, grid)
                consume(row, col + 1, grid); consume(row, col-1, grid)

        num_islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == '1':
                    grid = consume(row, col, grid)
                    num_islands += 1

class TestNumIslands(unittest.TestCase):
    def test_num_of_islands(self):
        pass

unittest.main(verbosity=2)
