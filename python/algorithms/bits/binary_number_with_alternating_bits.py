from typing import *

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        bits = f'{n:b}'
        prev = bits[0]
        print(bits)
        for i in range(1, len(bits)):
          if bits[i] == prev:
            return False
          else:
            prev = bits[i]
        return True

obj = Solution()
print(obj.hasAlternatingBits(5))

