from typing import *

class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        
        def shift(grid):
          prev = grid[-1][-1]
          for row in range(len(grid)):
            for col in range(len(grid[0])):
              temp = grid[row][col]
              grid[row][col] = prev
              prev = temp
          return grid
        
        for _ in range(k):
          grid = shift(grid)
        return grid

obj = Solution()
print(obj.shiftGrid([[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], 4))
    