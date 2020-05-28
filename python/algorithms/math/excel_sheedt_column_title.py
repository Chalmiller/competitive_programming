from typing import *

class Solution:
    def convertToTitle(self, n: int) -> str:
        letters = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
        result = ""
        
        while n:
            result = letters[(n - 1) % 26] + result
            n = (n - 1) // 26
        
        return result

obj = Solution()
print(obj.convertToTitle(702))
