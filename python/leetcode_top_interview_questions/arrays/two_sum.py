from typing import *

class Solution:
  def twoSum(self, nums: List[int], target: int) -> List[int]:
    cache = {}

    for i, num in enumerate(nums):
      target_num = target - num
      if target_num not in cache:
        cache[num] = i
      else:
        return [cache[target_num], i]
    return -1

