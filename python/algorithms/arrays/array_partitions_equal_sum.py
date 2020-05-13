from typing import *

class Solution:
    def canThreePartsEqualSum(self, A: List[int]) -> bool:
        total = sum(A)
        if total % 3 != 0:
          return False

        curr_sum = 0
        count = 0
        target = total // 3
        for num in A:
          curr_sum += num
          if curr_sum == target:
            count += 1
            curr_sum = 0
          
        return count >= 3

obj = Solution()
print(obj.canThreePartsEqualSum([10,-10,10,-10,10,-10,10,-10]))

