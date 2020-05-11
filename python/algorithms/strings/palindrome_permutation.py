from typing import *
from collections import Counter

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        my_counter = Counter(s)
        odds = 0
        for let, count in my_counter.items():
          if count % 2 == 1:
            odds += 1
        if odds < 2:
          return True
        return False

obj = Solution()
print(obj.canPermutePalindrome("aa"))