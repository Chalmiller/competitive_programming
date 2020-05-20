from typing import *

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        power = 1
        if n == 1:
          return True
        else:
          while power <= n:
            if power == n:
              return True
            else:
              power *= 2 
          return False

obj = Solution()
print(obj.isPowerOfTwo(16))