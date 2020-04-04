# 1200: Minimum Absolute Difference
from typing import *
from itertools import combinations

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort()
        mn = min(b - a for a, b in zip(arr, arr[1:]))
        return [[a,b] for a, b in zip(arr, arr[1:]) if b - a == mn]

obj = Solution()
num = obj.minimumAbsDifference([3,8,-10,23,19,-4,-14,27])
print(num)