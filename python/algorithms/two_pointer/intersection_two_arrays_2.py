# 350: Intersection of Two Arrays 2
from typing import *
from collections import Counter

class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        num1_counter = Counter(nums1)
        num2_counter = Counter(nums2)

        return list(((num1_counter & num2_counter).elements()))

        # 2 Pointer Method
        # nums1, nums2 = sorted(nums1), sorted(nums2)
        # pt1 = pt2 = 0
        # res = []

        # while True:
        #     try:
        #         if nums1[pt1] > nums2[pt2]:
        #             pt2 += 1
        #         elif nums1[pt1] < nums2[pt2]:
        #             pt1 += 1
        #         else:
        #             res.append(nums1[pt1])
        #             pt1 += 1
        #             pt2 += 1
        #     except IndexError:
        #         break

        # return res

obj = Solution()
num = obj.intersect([4,9,5], [9,4,9,8,4])
print(num)
