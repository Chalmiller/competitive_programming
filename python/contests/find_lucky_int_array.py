# 5368: Find Lucky Integer in an Array
from typing import *

class Solution:
    def findLucky(self, arr: List[int]) -> int:
        lucky_nums = []
        for num in arr:
            if num == arr.count(num):
                lucky_nums.append(num)
        if not len(lucky_nums):
            return -1
        else:
            return max(lucky_nums)
