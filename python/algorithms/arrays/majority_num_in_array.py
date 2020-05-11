from typing import *
import collections

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        num_count = collections.Counter(nums)
        return num_count[target] > len(nums)//2

obj = Solution()
print(obj.isMajorityElement([2,4,5,5,5,5,5,6,6], 5))