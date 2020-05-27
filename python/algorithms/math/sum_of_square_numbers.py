from typing import *
import math

class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        for i in range(c + 1):
            if i * i > c:
                return False
            if self.is_sq(c - i*i):
                return True
        return False
    
    def is_sq(self, v):
        i = math.sqrt(v)
        # print(i, int(i))
        if i == int(i):
            return True
        return False

obj = Solution()
print(obj.judgeSquareSum(5))
