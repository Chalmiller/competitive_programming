from typing import *

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        cache = {}

        for num in nums:
          if num not in cache:
            cache[num] = 1
          else:
            return True

        # one liner
        # return set(nums) == nums

obj = Solution()
print(obj.containsDuplicate([1,2,3,1]))
