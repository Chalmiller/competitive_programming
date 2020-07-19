import unittest

class Solution:
    def longestPalindrome(self, s: str) -> str:
        """
        Task: within a given string, find the longest substring.
        Intuition: I think this can be done by a two pointer method

        Algorithm: 
          1. have one pointer at the end and one at the beginning
          2. slice each step
        """
        if len(s) < 3:
            if s[::-1] == s:
                return s
            else:
                return s[0]
        max_length = ""
        for i in range(len(s) - 1):
            for j in range(i+1, len(s)):
                # O(n)
                new_slice = s[i:j+1]
                if new_slice == new_slice[::-1]:
                    if len(new_slice) > len(max_length):
                        max_length = new_slice
        return max_length if len(max_length) > 1 else s[0]
            
class TestSolution(unittest.TestCase):
    
    def is_one_character(self):
        a = "a"
        self.assertTrue(Solution().longestPalindrome(a))
        
if __name__ == "__main__":
    unittest.main()