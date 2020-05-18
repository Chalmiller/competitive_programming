from typing import *
import math
import collections

class Solution:
    def findLHS(self, nums: List[int]) -> int:
      counter = collections.Counter(nums)
      ans = 0

      for x in nums:
        if x+1 in counter:
          ans = max(ans, counter[x] + counter[x+1])
      return ans
      