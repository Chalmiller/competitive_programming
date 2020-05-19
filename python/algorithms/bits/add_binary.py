from typing import *

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        dec_1 = 0
        dec_2 = 0
        for i in range(len(a)):
          dec_1 += int(a[i]) * 2**(len(a)-(1 + i))
        
        for i in range(len(b)):
          dec_2 += int(b[i]) * 2**(len(b) - (1 + i))

        _sum = dec_1 + dec_2
        return f'{_sum:b}'

obj = Solution()
print(obj.addBinary("1010", "1011"))