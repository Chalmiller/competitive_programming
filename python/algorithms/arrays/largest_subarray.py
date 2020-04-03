# 30 Day Coding Challenge
from typing import *
from sys import maxint

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        arr_size = len(nums)
        local_max = nums[0]
        global_max = nums[0]
        
        for i in range(1, arr_size):
            local_max = max(nums[i], nums[i] + local_max)
            global_max = max(global_max, local_max)
            
        return global_max