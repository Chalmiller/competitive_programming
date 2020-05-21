from typing import *
import math
import itertools

class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
      ans = 0

      for seat, group in itertools.groupby(seats):
        print(seat, list(group))
        if not seat:
          k = len(list(group))
          ans = max(ans, (k+1)//2)

obj = Solution()
print(obj.maxDistToClosest([1,0,0,0,1,0,1]))