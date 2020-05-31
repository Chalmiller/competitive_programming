from typing import *

class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:
        sorted_nums = sorted(nums)

        i, j = 0, len(nums) - 1

        while i < j:
          if sorted_nums[i] == nums[i]:
            i += 1
          if sorted_nums[j] == nums[j]:
            j += 1
          if not (sorted_nums[j] == nums[j]) and not (sorted_nums[i] == nums[i]):
            return j - i
        return 0