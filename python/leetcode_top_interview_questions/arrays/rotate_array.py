from typing import *

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k == 0:
          return
        else:
          nums = nums[-1] + nums[:-1]
          return self.rotate(nums, k-1)