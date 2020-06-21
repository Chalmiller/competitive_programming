from typing import *

class Solution:
    def rotate(self, nums, k):
        """
        Task: rotate the array by k steps
        Intuition: This can be done recursively or iteratively

        Algorihtm:
        1. iterate through the array
        2. pop the end off and append it to the beginning ofthe array
        """
        # for _ in range(k):
        #   temp = nums.pop()
        #   nums = [temp] + nums
        # return nums
        
        if k == 0:
            return nums
        else:
            return [nums[-1]] + self.rotate(nums[:-1], k-1)

obj = Solution()
print(obj.rotate([1,2,3,4,5,6,7], 3))