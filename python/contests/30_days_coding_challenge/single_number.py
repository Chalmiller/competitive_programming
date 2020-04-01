# 30 Day Coding Challenge Day 1
from typing import *

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        # Brute Force
        for num in nums:
            if nums.count(num) < 2:
                return num
