from typing import *

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
      if n < 3:
        return False
      
      
      num = 1
      while num <= n:
        if num == n:
          return True
        num *= 3
      
      return False

obj = Solution()
print(obj.isPowerOfThree(45))