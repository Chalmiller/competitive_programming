from typing import *

class Solution:
  def mySqrt(self, x: int) -> int:
    for i in range(x):
      if i*i == x:
        return i
      elif i*i > x:
        return i-1

obj = Solution()
print(obj.mySqrt(79))
