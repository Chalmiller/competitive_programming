from typing import *

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        answer = [False] * len(A)
        total = 0

        for i in range(len(A)):
          total += A[i]

          if total % 5 == 0:
            answer[i] = True

          total = total << 1
          
        return answer

obj = Solution()
print(obj.prefixesDivBy5([0,1,1,1,1,1]))