from typing import *

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def consume_island(i, j, grid):
          if i < 0 or j < 0 or i == len(grid) or j == len(grid[0]):
            return
          else:
            grid[i][j] = '0'
          consume_island(i+1,j, grid)
          consume_island(i-1,j, grid)
          consume_island(i,j+1, grid)
          consume_island(i,j-1, grid)

        islands = 0
        for row in range(len(grid)):
          for col in range(len(grid[0])):
            if grid[row][col] == '1':
              islands += 1
              consume_island(row, col, grid)
        return islands
        