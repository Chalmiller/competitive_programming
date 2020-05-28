from typing import *

class Solution:
    def thirdMax(self, nums: List[int]) -> int:
        _max = max(nums)

        if len(nums) < 3:
          return _max

        for _ in range(2):
          nums.remove(_max)
          _max = max(nums)
          
        return _max

