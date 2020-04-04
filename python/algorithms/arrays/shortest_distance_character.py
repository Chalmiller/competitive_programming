# 821: Shortest Distance to a Character
from typing import *

class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        # Find all indices where the character occurs in the string
        indices = [index for index, char in enumerate(S) if char == C]
        res = []
        for index in range(len(S)):
            res.append(min([abs(index - num) for num in indices]))
        return res
        

obj = Solution()
num = obj.shortestToChar("loveleetcode", 'e')
print(num)