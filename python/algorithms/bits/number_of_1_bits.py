from typing import *

class Solution:
    def hammingWeight(self, n: int) -> int:
        
        bits = str(n)
        result = [int(i) for i in bits if i == '1']
            
        return sum(result)

obj = Solution()
print(obj.hammingWeight("00000000000000000000000000001011"))
