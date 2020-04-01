# 461: Hamming Distance
from typing import *
from itertools import permutations

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        x = x ^ y
        y = 0
        while x:
            y += 1
            x = x & (x - 1)
        return y

obj = Solution()
num = obj.hammingDistance(1, 4)
print(num)