from typing import *
import unittest

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
      dp = grid
      for row in range(1, len(grid)):
        for col in range(1, len(grid[0])):
          dp[row-1][col-1] = grid[row-1][col-1] + min(grid[row-1][col], grid[row][col-1])
      return dp[-1][-1]


class MinPathSumTest(unittest.TestCase):

  def test_min_sum(self):
    input = [[1,3,1],[1,5,1],[4,2,1]]
    output = 7
    self.assertEqual(output, Solution().minPathSum(input))

unittest.main(verbosity=2)