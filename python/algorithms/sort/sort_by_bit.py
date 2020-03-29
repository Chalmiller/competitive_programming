# 1356: Sort Integers by the Number of 1 Bits
from typing import *
from functools import reduce

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr, key = lambda num: (sum((num >> i) & 1 for i in range(32)), num))

obj = Solution()
listy = obj.sortByBits([1024,512,256,128,64,32,16,8,4,2,1])
print(listy)
