from typing import *

def canJump(self, nums):
    max_reach, n = 0, len(nums)
    for i, x in enumerate(nums):
        if max_reach < i: return False
        if max_reach >= n - 1: return True
        max_reach = max(max_reach, i + x)

obj = Solution()
obj.canJump([3,2,1,0,4])
print(obj)