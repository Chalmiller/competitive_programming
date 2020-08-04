from typing import *
import unittest

class Solution:
    def findMin(self, nums: List[int]) -> int:
        """
        Task: Find the pivot point of the rotated sorted array
        Intuition: Modified binary Search problem

        Algorithm: 
            - brute force:
                - iterate through the array until arr[i] < arr[i-1]
                - return arr[i]

        Time Complexity - O(n)
        Space - O(1)
        """

        # for i in range(1, len(nums)):
        #     if nums[i] < nums[i-1]:
        #         return nums[i]
        # return nums[0]

        # Binary search method

        l, r = 0, len(nums) - 1
        if nums[r] > nums[l]:
            return nums[0]

        while l <= r:
            mid = l + (r-l)//2
            if nums[mid-1] > nums[mid]:
                return nums[mid]
            elif nums[mid+1] < nums[mid]:
                return nums[mid]
            elif nums[mid] > nums[0]:
                l = mid+1
            else:
                r = mid - 1
        

class TestFindMin(unittest.TestCase):

    def test_find_min(self):
        input = [0,1,2,3,4,5]
        output = 0
        self.assertEqual(output, Solution().findMin(input))

unittest.main(verbosity=2)
