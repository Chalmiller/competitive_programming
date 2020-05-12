from typing import *
import math

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
      count = 0
      _max = -math.inf
      for num in nums:
        if num != 1:
          count = 0
        else:
          count += 1
          _max = max(_max, count)
      return max(count, _max)


obj = Solution()
print(obj.findMaxConsecutiveOnes([0, 1]))
