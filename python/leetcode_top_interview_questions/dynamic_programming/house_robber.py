from typing import *
import unittest

class Solution:
    def rob(self, nums: List[int]) -> int:
        curr = 0
        prev = 0

        for el in nums:
            temp = curr
            curr = max(prev+el, curr)
            prev = temp
        
class TestHouserobber(unittest.TestCase):
    def test_house_robber(self):
        pass

unittest.main(verbosity=2)
