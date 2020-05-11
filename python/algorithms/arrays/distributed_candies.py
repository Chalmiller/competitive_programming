from typing import *
import collections

class Solution:
    def distributeCandies(self, candies: List[int]) -> int:
      return min(len(candies) / 2, len(set(candies)))

obj = Solution()
print(obj.distributeCandies([1,1,2,3]))
          
