from typing import *
import unittest

class Solution:
    def numDecodings(self, s: str) -> int:
        """
        Task: return the number of ways a input number can be decoded
        Inutuition: This is a number of ways dynamic programming problem

        Algorithm: 
            - Basically, for each individual number in the input, we can decode it individually or group it together with another number
            - Similar to the two stairs question, we basically count up dynamically
        """
        if not s:
            return 0
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1
        dp[1] = 0 if s[0] == '0' else 1

        for i in range(2, len(dp)):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            two_digit = int(s[i-2:i])
            if two_digit >= 10 and two_digit <= 26:
                dp[i] += dp[i-2]
        return dp[len(s)]

class TestNumdecodings(unittest.TestCase):

    def test_working_solution(self):
        pass

unittest.main(verbosity=2)