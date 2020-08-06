from typing import *
import unittest
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        self.found = False
        @lru_cache(None)
        def dfs(s):
            if len(s) == 0:
                self.found = True
                return True
            for word in wordDict:
                if word == s[0:len(word)]:
                    dfs(s[len(word):])
        
        dfs(s)
        return self.found

class TestWordBreak(unittest.TestCase):
    def test_word_break(self):
        pass

unittest.main(verbosity=2)
