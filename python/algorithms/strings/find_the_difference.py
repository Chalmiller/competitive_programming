from typing import *
import collections

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        set_s = collections.Counter(s)
        set_t = collections.Counter(t)
        return list(set_t - set_s)[0]

obj = Solution()
print(obj.findTheDifference("abcd", "abcde"))