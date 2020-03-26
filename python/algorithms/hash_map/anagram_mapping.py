# 760: Find Anagram Mapping
from typing import *

class Solution:
    def anagramMappings(self, A: List[int], B: List[int]) -> List[int]:
        return [B.index(i) for i in A]

obj = Solution()
num = obj.anagramMappings([12, 28, 46, 32, 50], [50, 12, 32, 46, 28])
print(num)