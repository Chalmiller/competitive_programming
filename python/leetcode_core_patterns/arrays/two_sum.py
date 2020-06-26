from typing import *

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    """
    Task: Return two numbers that add to a specific target
    """

    for i in range(len(nums)):
      curr_needed = abs(nums[i]-target)
      for j in range(1,len(nums)):
        if nums[j] == curr_needed:
          return [i, j]

obj = Solution()
print(obj.twoSum([2, 7, 11, 15], 9))