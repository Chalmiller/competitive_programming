# 1304: Find N Unique Integers Sum up to Zero
from typing import *

class Solution:
    def sumZero(self, n: int) -> List[int]:
        if n % 2 == 1:
            start = (n - 1)//2
            return [i for i in range(-start, start+1)]
        else:
            start = n//2
            even_list = [i for i in range(-start, 0)]
            even_list.extend([j for j in range(1, start + 1)])
            print(even_list)
            return even_list
obj = Solution()
obj.sumZero(4)
        