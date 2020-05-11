from typing import *

class Solution:
    def binaryGap(self, N: int) -> int:
        bits = f'{N:b}'
        res = [i for i, el in enumerate(bits) if el == '1']
        _max = 0
        print(res)

        for i in range(len(res) - 1):
          _max = max(_max, abs(res[i + 1] - res[i]))
        return _max
        
obj = Solution()
print(obj.binaryGap(15))