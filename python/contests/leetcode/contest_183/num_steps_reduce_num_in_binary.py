from typing import *

class Solution:
    def numSteps(self, s: str) -> int:
        binary_to_int = int(s, 2)
        count = 0
        while binary_to_int != 1:    
            if binary_to_int % 2 == 0:
                binary_to_int //= 2
            else:
                binary_to_int += 1
            count += 1
        return count


obj = Solution()
num = obj.numSteps("1111011110000011100000110001011011110010111001010111110001")
print(num)