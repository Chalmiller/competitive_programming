from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # two pointer solution
        point_1 = 0
        point_2 = 0
        array_length = len(nums)

        while point_1 < array_length - 1:

          curr_el = nums[point_1]

          while nums[point_2] == curr_el:
            point_2 += 1
          point_1 += 1
          nums = nums[:point_1] + nums[point_2:]
          point_2 = point_1
          array_length = len(nums)

          
        return nums

        x = 1
        for i in range(len(nums) - 1):
          if (nums[i] != nums[i + 1]):
            nums[x] = nums[i + 1]
            x += 1
        return x

obj = Solution()
print(obj.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))