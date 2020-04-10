# 167: Two Sum 2 - Input Array is Sorted
from typing import *

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        low = 0
        high = len(numbers) - 1

        while low < high:
          curr_sum = numbers[low] + numbers[high]
          if curr_sum > target:
            high -= 1
            continue
          elif curr_sum < target:
            low += 1
            continue
          else:
            return [low+1, high+1]
        return -1

