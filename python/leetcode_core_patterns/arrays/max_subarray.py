from typing import *

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      """Kadanes greedy algorithm"""
      if not nums:
        return nums

      max_here = nums[0]
      max_so_far = nums[0]

      for i in range(1, len(nums)):
        max_here = max(nums[i], max_here + nums[i])
        max_so_far = max(max_so_far, max_here)
      return max_so_far

