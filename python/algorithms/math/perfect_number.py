from typing import *
import math

class Solution:
    def checkPerfectNumber(self, num: int) -> bool:
        if num<2: return False
        primes=[2,3,5,7,13,17,19,31]
        for prime in primes:
            if (2**(prime-1))*((2**prime)-1)==num:
                return True
        return False

obj = Solution()
print(obj.checkPerfectNumber(28))
        
