from typing import *
import math

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        index = 0
        _max = -math.inf
        count = 1 if len(nums) > 0 else 0

        while index < len(nums) - 1:
          if nums[index] < nums[index+1]:
            count += 1
            _max = max(count, _max)
          else:
            _max = max(count, _max)
            count = 1
          index += 1  
            
        return max(_max, count)

obj = Solution()
print(obj.findLengthOfLCIS([1,3,5,7]))