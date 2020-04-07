# 1176: Diet Plan Performance
from typing import *
import itertools

class Solution:
    def dietPlanPerformance(self, calories: List[int], k: int, lower: int, upper: int) -> int:
        points, win = 0, sum(itertools.islice(calories, k - 1))
        for i, calory in enumerate(itertools.islice(calories, k -1, None), k - 1):
            win += calory - (i >= k) * calories[i - k]
            points += (win > upper) - (win < lower)
        return points

obj = Solution()
num = obj.dietPlanPerformance([1,2,3,4,5], 1, 3, 3)
print(num)
