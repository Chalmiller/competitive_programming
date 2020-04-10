# 349: Intersection of Two Arrays
from typing import *

class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
      # One Liner
      # return list({num for num in nums1 if num in nums1 and num in nums2})
      # return list(set(nums1) & set(nums2))

      # Two Pointer Solution
      num_set = {}
      for i in range(len(nums1)):
        if nums1[i] == nums2[i]:
          num_set.add(nums1[i])
      return list(num_set)

obj = Solution()
num = obj.intersection([4,9,5], [9,4,9,8,4])
print(num)