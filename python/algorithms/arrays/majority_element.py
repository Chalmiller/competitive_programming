from typing import *
import collections

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        num_counter = collections.Counter(nums)
        for num in nums:
          if num_counter[num] > len(nums)//2:
            return num