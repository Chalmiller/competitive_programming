from typing import *

class Solution:
    def validMountainArray(self, A: List[int]) -> bool:
        zenith = max(A)
        zenith_index = A.index(zenith)

        for i in range(zenith_index - 1):
          if A[i] >= A[i+1]:
            return False
        
        for j in range(zenith_index, len(A) - 1):
          if A[j] <= A[j+1]:
            return False
        
        return True

obj = Solution()
print(obj.validMountainArray([3,5,5]))
