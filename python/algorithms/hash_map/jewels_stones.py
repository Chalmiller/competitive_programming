# 771 - Jewels and Stones
from typing import *

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        stone_map = set(J)
        count = 0

        for jewel in S:
            if jewel in stone_map:
                count += 1
        return count
        # one liner
        # return sum(map(J.count, S))

obj = Solution()
num = obj.numJewelsInStones("aA", "aAAbbbb")
print(num)