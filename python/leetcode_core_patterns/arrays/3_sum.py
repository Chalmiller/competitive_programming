import unittest
from typing import *

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        found, dups = set(), set()
        seen = {}
        for i, val1 in enumerate(nums):
            if val1 not in dups:
                dups.add(val1)
                for j, val2 in enumerate(nums[i+1:]):
                    complement = -val1 - val2
                    if complement in seen and seen[complement] == i:
                        min_val = min((val1, val2, complement))
                        max_val = max((val1, val2, complement))
                        if (min_val, max_val) not in found:
                            found.add((min_val, max_val))
                            res.append([val1, val2, complement])
                    seen[val2] = i
        return res

class TestThreeSum(unittest.TestCase):

  def three_sum(self):
    array = [-1, 0, 1, 2, -1, -4]
    output = [[-1,1,0],[-1,-1,2]]
    self.assertEquals(output, Solution().threeSum(array))

if __name__ == "__main__":
  unittest.main()