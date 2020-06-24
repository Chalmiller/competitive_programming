from typing import List
from collections import deque

class Solution:
  def permute(self, nums: List[int]) -> List[List[int]]:
    """
    Task: Generate all valid permutations from a given list

    Algorith:
      1. breadth first search
    """
    def backtrack(first = 0):
      if first == n:
        output.append(nums[:])

      for i in range(first, n):
        nums[first], nums[i] = nums[i], nums[first]
        backtrack(first + 1)
        nums[first], nums[i] = nums[i], nums[first]

    n = len(nums)
    output = []
    backtrack()
    return output


