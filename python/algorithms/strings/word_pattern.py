from typing import *

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern):
            return False
        word_to_pattern = {} # {'dog': 'a', 'cat': 'b'}
        pattern_to_word = {} # {'a': 'dog', 'b': 'cat'}
        for i in range(len(s)):
            if s[i] not in word_to_pattern:
                word_to_pattern[s[i]] = pattern[i]
            if pattern[i] not in pattern_to_word:
                pattern_to_word[pattern[i]] = s[i]
            if  pattern_to_word[pattern[i]] != s[i] or word_to_pattern[s[i]] != pattern[i]:
                return False
        return True

obj = Solution()
print(obj.wordPattern("abba", "dog dog dog dog"))
