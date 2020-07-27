from typing import *
import unittest
import math

class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
      """
      Task: Given a grid, find the shortest path to the bottom right.
      Intuition: This is obviously indicated as being DP because of the 
                problem statement, but I wonder if one could use Dijkstras?

      Algorihtm: 
        - modify the row and col to be the total path to traverse.
        - iterate through the grid, summing the path of least resistance.

      Time Complexity: O(n^2) if the grid is a square, otherwise O(n*m)
      Space: O(n*m) because we hold the values of the grid
      """

      dp = grid[:]
      for i in range(1, len(grid[0])):
        dp[0][i] = dp[0][i-1] + grid[0][i]

      print(dp)

      for j in range(1, len(grid)):
        dp[j][0] = dp[j-1][0] + grid[j][0]

      print(dp)

      for row in range(1, len(grid)):
        for col in range(1, len(grid[0])):
          grid[row][col] = grid[row][col] + min(grid[row-1][col], grid[row][col-1])
      print(grid)    
      return grid[-1][-1]

    def minPathSumRecursive(self, grid: List[List[int]]) -> int:

      def calculate(grid, i, j):
        if i == len(grid) or j == len(grid[0]): return math.inf
        if i == len(grid - 1 or j == len(grid[0] - 1)): return grid[i][j]
        return grid[i][j] + min(calculate(grid, i+1, j), calculate(grid, i, j+1))
      
      return calculate(grid, 0, 0)

class MinPathSumTest(unittest.TestCase):

  def test_min_sum(self):
    input = [[1,3,1],[1,5,1],[4,2,1]]
    output = 7
    self.assertEqual(output, Solution().minPathSum(input))
  
  def test_recursive_solution(self):
    input = [[1,3,1], [1,5,1], [4,2,1]]
    output = 7 
    self.assertEqual(output, Solution().minPathSumRecursive(input))

unittest.main(verbosity=2)