from typing import *

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        """
        Task: Find where the two arrays intersect

        Algorithm:
          1. they dont need to match - smh
        """

        res, cache = [], {}

        for num in nums1:
          cache[num] = cache.get(num, 0) + 1

        for num in nums2:
          if num in cache and cache[num] > 0:
            res.append(num)
            cache[num] -= 1
        return res