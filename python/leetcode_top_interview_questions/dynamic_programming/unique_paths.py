from typing import *
import unittest

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        """
        Task: How many unique paths are there to guide the robot from the start to finish
        Intuition: I think this is a backtracking problem, but I'm unsure of its implementation

        Algorithm: 
            * I need to consult a solution and pseudo code it out.

            - generate an array to encapsulate the example array
            - for each cell in the array, the total number of paths to get to it is
                the total of the paths above it and to the left of it
            return dp[n-1]m-1]
        """
        dp = [[1] * n for _ in range(m)]

        for col in range(1, n):
            for row in range(1, m):
                dp[row][col] = dp[row-1][col] + dp[row][col-1]
        return dp[m-1][n-1]

class TestUniwuePaths(unittest.TestCase):

    def test_unique_paths(self):
        rows, cols = 3, 7
        result = 28
        self.assertEqual(result, Solution().uniquePaths(rows, cols))

unittest.main(verbosity=2)
