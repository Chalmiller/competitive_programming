from typing import *

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        left_sum = 0
        right_sum = sum(nums)

        for index in range(len(nums)):
          right_sum -= nums[index]
          if left_sum == right_sum:
            return index
          left_sum += nums[index]
        return -1

obj = Solution()
print(obj.pivotIndex([-1,-1,0,1,1,0]))