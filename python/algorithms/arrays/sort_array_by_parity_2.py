# 922: Sort array by Parity 2
from typing import *

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        res = [0] * len(A)
        even_steps = 0
        odd_steps = 1
        
        for el in A:
            if el % 2 == 0:
                res[even_steps] = el
                even_steps += 2
            else:
                res[odd_steps] = el
                odd_steps += 2
        return res

obj = Solution()
num = obj.sortArrayByParityII([4,2,5,7])
print(num)
