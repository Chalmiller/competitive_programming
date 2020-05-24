from typing import *

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        i, j = 0, 0
        while i < m + n:
          if nums1[i] <= nums2[j] and nums1[i] != 0:
            i += 1
          elif nums1[i] == 0:
            nums1.insert(i, nums2[j])
            j += 1
            i += 1
          elif nums1[i] > nums2[j]:
            nums1.insert(i, nums2[j])
            j += 1
            i += 1
        nums1 = nums1[:m+n]
        return nums1

obj = Solution()
print(obj.merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))          

