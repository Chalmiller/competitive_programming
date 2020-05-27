from typing import *

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        for i in range(k):
          nums = list(nums[-1:]) + nums[:len(nums)-1]
        print(nums)

obj = Solution()
print(obj.rotate([1,2,3,4,5,6,7], 3))
