from typing import *
import unittest

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        """
        Task: Find the longest consecutive sequence of integers in an unsorted array
        Intuition: I had to check the related topics, but this is apparently a union find
        """
        longest_streak = 0
        num_set = set(nums)

        for num in num_set:
            if num - 1 not in nums:
                curr_num = num
                curr_streak = 1

                while curr_num + 1 in num_set:
                    curr_num += 1
                    curr_streak += 1
                
                longest_streak = max(longest_streak, curr_streak)
        return longest_streak


class TestLongestConsecutiveSequence(unittest.TestCase):
    def test_longest_consec_sequence(self):
        pass

unittest.main(verbosity=2)
