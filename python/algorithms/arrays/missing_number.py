from typing import *

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        expected_sum = len(nums) * (len(nums) + 1)//2
        actual_sum = sum(nums)
        return expected_sum - actual_sum

obj = Solution()
print(obj.missingNumber([9,6,4,2,3,5,7,0,1]))