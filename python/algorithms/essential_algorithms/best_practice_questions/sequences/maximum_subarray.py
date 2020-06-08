import math

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
      """
      1. keep track of the sum for each element in the list
      2. if the sum dips below 0, reset the sum
      3. if the sum is greater than the global sum, set the global sum
      """
      max_so_far = -math.inf
      max_here = 0

      for num in nums:
        max_here += num
        if max_here < 0:
          max_here = 0
        if max_so_far < max_here:
          max_so_far = max_here
      return max_so_far