from typing import *

class Solution:
    def isMonotonic(self, A: List[int]) -> bool:
        is_increasing = True if A[0] < A[-1] else False
        print(is_increasing)
          
        for i in range(len(A) - 1):
          if A[i] <= A[i + 1] and is_increasing:
            continue
          elif A[i] >= A[i + 1] and not is_increasing:
            continue
          else:
            return False
        return True

obj = Solution()
print(obj.isMonotonic([1,1,0]))

          