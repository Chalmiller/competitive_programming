from typing import *
import operator
import functools

class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
      left_right_skyline = [max(els) for els in grid]
      top_bot_skyline = [max(els) for els in zip(*grid)]

      def flatten(matrix):
        flatten_matrix = [el for rows in matrix for el in rows]
        return flatten_matrix
      
      new_buildings = [[] for _ in range(len(grid))]
      for lr in range(len(left_right_skyline)):
        for tb in range(len(top_bot_skyline)):
          _min = min(left_right_skyline[lr], top_bot_skyline[tb])
          new_buildings[lr].append(_min)
      # sum both grids and return the difference of the two
      
      total_1 = functools.reduce(operator.add, flatten(grid))
      total_2 = functools.reduce(operator.add, flatten(new_buildings))
      return abs(total_1 - total_2)

obj = Solution()
print(obj.maxIncreaseKeepingSkyline([[3,0,8,4],[2,4,5,7],[9,2,6,3],[0,3,1,0]]))
