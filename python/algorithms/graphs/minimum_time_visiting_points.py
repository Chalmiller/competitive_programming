# 1266: Minimum Time Visiting All Points
from typing import *

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        for index in range(1, len(points)):
            count += max(abs(points[index][0] - points[index - 1][0]), abs(points[index][1] - points[index - 1][1]))
        return count
            
obj = Solution()
num = obj.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
print(num)