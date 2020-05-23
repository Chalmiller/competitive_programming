from typing import *
import math

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        running = sum(nums[:k])
        res = running / k
        for i in range(0, len(nums)-k):
            running -= nums[i]
            running += nums[i+k]
            res = max(res, running / k)
        return res


obj = Solution()
print(obj.findMaxAverage([1,12,-5,-6,50,3], 4))

