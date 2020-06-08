from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        """
        Task: Find all unique triplets that sum to 0
        Intuition: 
          - a + b = -c
          - having three pointers is a brute force approach
            - would be O(n^2)
        Using three pointer approach:
        1. for each element in the array, for loop after it
        2. if there are two numbers that then add up to -element, we have a triplet, so store in a set
        3. return the set as a converted list to match the return value

        Edge Cases:
          - the set is empty
          
        Time Complexity:
          - O(n^2)
          - O(n/3)
        """
        res_set = set()   
        response = []     
        nums.sort()
        # [-4, -1, -1, 0, 1, 2]
        for i in range(len(nums) - 1):
          target = -nums[i] # +1
          ptr1 = i + 1
          ptr2 = len(nums) - 1
          
          while ptr1 < ptr2:
            curr_sum = nums[ptr1] + nums[ptr2]
            if curr_sum < target:
              ptr1 += 1
            elif curr_sum > target:
              ptr2 -= 1
            else:
              triplet = (-target, nums[ptr1], nums[ptr2])
              res_set.add(triplet)
              ptr1 += 1
              ptr2 -= 1

        for tup in res_set:
          response.append(list(tup))

        return response

obj = Solution()
print(obj.threeSum([-1, 0, 1, 2, -1, -4]))
          