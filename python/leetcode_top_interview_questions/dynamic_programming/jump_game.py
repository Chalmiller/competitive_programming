from typing import *
import unittest

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        max_reach, n = 0, len(nums)
        for i, num in enumerate(nums):
            if max_reach < i:
                return False
            if max_reach >= n-1:
                return True
            max_reach = max(max_reach, i+num)


class TestJumpGame(unittest.TestCase):

    def test_can_jump(self):
        nums = [3,2,1,0,4]
        self.assertTrue(Solution().canJump(nums), "Should be True")

unittest.main(verbosity=2)