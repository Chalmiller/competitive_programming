from typing import *

class Solution:
    def minSubsequence(self, nums: List[int]) -> List[int]:
        nums.sort()
        arr_size = len(nums)
        local_max = nums[0]
        global_max = nums[0]
        
        for i in range(1, arr_size):
            local_max = max(nums[i], nums[i] + local_max)
            global_max = max(global_max, local_max)
        return global_max