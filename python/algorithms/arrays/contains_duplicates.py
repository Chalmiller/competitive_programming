from typing import *
import collections

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        num_counter = collections.Counter(nums)
        for el, count in num_counter.items():
          if count > 1:
            return True
        return False