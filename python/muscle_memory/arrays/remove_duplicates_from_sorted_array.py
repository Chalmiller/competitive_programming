from typing import *

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        """
        Task: Remove duplicates in place
        Intuition: This can be solved several ways. One being two pointer, the other being with a hashmap

        Algorithm:
        1. iterate through array
        2. add each element to a dictionary
        3. if the curr_el is already in the dictionary, del the current index
        """

        # cache = {}
        # i, n = 0, len(nums) - 1 
        # # [1,1]
        # while i < n:
        #   print(i, cache)
        #   if nums[i] not in cache:
        #     cache[nums[i]] = 1
        #     i += 1
        #   else:
        #     del nums[i]
        #     n -= 1
            
        # return len(nums)

        # Two Pointer Solution
        if len(nums) == 0:
          return 0
        i = 0
        for j in range(1, len(nums)):
          if nums[j] != nums[i]:
            i += 1
            nums[i] = nums[j]
        return i + 1


obj = Solution()
print(obj.removeDuplicates([1,1]))