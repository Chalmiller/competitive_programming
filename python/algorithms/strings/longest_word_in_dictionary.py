from typing import *
import collections
import copy
import math

class Solution:
    def longestWord(self, words: List[str]) -> str:
        ans = ''
        wordset = set(words)
        print(wordset)

        for word in words:
          if len(word) > len(ans) or len(word) == len(ans) and word < ans:
            print(list(word[:k] for k in range(1, len(word))))
            if all(word[:k] in wordset for k in range(1, len(word))):
              ans = word
        return ans

        
obj = Solution()
print(obj.longestWord(["w","wo","wor","worl", "world"]))