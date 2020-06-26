from typing import *

class Solution:
  def containsDuplicate(self, nums: List[int]) -> bool:
      cache = {}

      for num in nums:
        cache[num] = cache.get(num, 0) + 1
        if cache[num] > 1:
          return True
      return False

obj = Solution()
print(obj.containsDuplicate([1,2,3]))
