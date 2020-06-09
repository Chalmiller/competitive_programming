from typing import *
import math

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        """
        Task: Find the largest contiguous subarray product

        Intuition: 
          - This is very much like the Kadanes algorithm problem. I'll try solving 
            it that way first

        Approach:
          1. start with the first item of the list and generate a max_so_far and max_here
          2. iterate through the array taking the max of max_here * array[i] and max_so_far
          3. return max_so_far
        """
        if not nums:
          return nums

        prefix = 0
        suffix = 0
        max_so_far = -math.inf
        # [-2,0,-1]
        for i in range(len(nums)):
          prefix = (prefix or 1) * nums[i]
          suffix = (suffix or 1) * nums[~i]
          max_so_far = max(prefix, suffix, max_so_far)

        return max_so_far

obj = Solution()
print(obj.maxProduct([2,3,-2,4]))
