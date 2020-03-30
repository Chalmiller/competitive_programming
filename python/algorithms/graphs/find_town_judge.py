# 997: Find the Town Judge
from collections import defaultdict
from typing import *

class Solution:
    def findJudge(self, N: int, trust: List[List[int]]) -> int:
        count = [0] * (N + 1)
        for i, j in trust:
            count[i] -= 1
            count[j] += 1
        print(count)
        for i in range(1, N + 1):
            if count[i] == N - 1:
                return i
        return -1

obj = Solution()
num = obj.findJudge(3, [[1,3],[2,3]])
print(num)