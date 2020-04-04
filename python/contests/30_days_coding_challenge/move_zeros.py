# Leetcode 30 day challenge
from typing import *
from collections import Counter

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        zero_count = Counter(nums)
        for num in range(zero_count[0]):
            nums.remove(0)
        nums.extend([0]*zero_count[0])
        print(nums)

obj = Solution()
nums = obj.moveZeroes([1,0,3,2,1,0,0,0])
print(nums)