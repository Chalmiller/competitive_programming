from typing import *
import unittest
import math

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        """
        Task: Return the minimum length string from S that includes all the values within T
        Intuition: This is constricted to O(n) time, so the brute force solution probably won't work.
                    My brute force approach would be to use a two pointer approach and remove elements 
                    from it as we move along.

        Algorithm:
            - generate a counter for T |
                                                      | => both of these can come from a functional component
            - generate a counter for S | 
            - start both pointers at the beginning of the array
                - if either of the pointers points to an element not in T, move up or down that pointer
                - if all elements are in the array, start reducing the size until you can't anymore
        """
        if not t or not s:
            return ""

        def generate_counter(string):
            str_dict = {}
            for let in string:
                str_dict[let] = str_dict.get(let, 0) + 1
            return str_dict

        dict_t = generate_counter(t)

        required = len(dict_t)

        l, r = 0, 0
        formed = 0

        window_counts = {}
        ans = math.inf, None, None

        while r < len(s):
            character = s[r]
            window_counts[character] = window_counts.get(character, 0) + 1

            if character in dict_t and window_counts[character] == dict_t[character]:
                formed += 1

            while l <= r and formed == required:
                character = s[l]

                if r - l + 1 < ans[0]:
                    ans = (r-l+1, l, r)
                window_counts[character] -= 1
                if character in dict_t and window_counts[character] < dict_t[character]:
                    formed -= 1
                l += 1
            r == 1
        return "" if ans[0] == math.inf else s[ans[1] : ans[2] + 1]


class TestMinWindow(unittest.TestCase):

    def test_working_solution(self):
        pass

unittest.main(verbosity=2)
