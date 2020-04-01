# 1385: Find Distance Value Between Two Arrays
from typing import *

class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        print([[(i, j) for i in arr2] for j in arr1])
        return sum(all(abs(i - j) > d for j in arr2) for i in arr1)

obj = Solution()
num = obj.findTheDistanceValue([1,4,2,3], [-4,-3,6,10,20,30], 3)
print(num)