from typing import *
import unittest
from functools import lru_cache

class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        trie = {}

        for word in wordDict:
            node = trie
            for c in word:
                if c not in node:
                    node = node[c]
            node[None] = True
        print(node)
        
        @lru_cache(None)
        def dp(idx):
            if idx >= len(s):
                return True
            if s[idx] not in trie:
                return False
            node = trie
            while idx < len(s) and s[idx] in node:
                node = node[s[idx]]
                idx += 1
                if None in node:
                    if dp(idx):
                        return True
            return False

        return dp(0)

class TestWordBreak(unittest.TestCase):
    def test_word_break(self):
        pass

unittest.main(verbosity=2)
