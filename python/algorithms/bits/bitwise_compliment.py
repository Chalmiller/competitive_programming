from typing import *

class Solution:
    def bitwiseComplement(self, N: int) -> int:
        bits = f'{N:b}'
        response_builder = ""
        for bit in bits:
          if bit == '1':
            response_builder = response_builder + '0'
          else:
            response_builder = response_builder + '1'
        return int(response_builder, 2)

obj = Solution()
print(obj.bitwiseComplement(7))