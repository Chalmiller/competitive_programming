from typing import *
import collections

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        string_set = set(t)

        for el in string_set:
          if el not in s:
            t = t.replace(el, '')
        # iterate over the edited string and match each distinct character
        print(t)
        if len(t) < len(s):
          return False
        return collections.OrderedDict.fromkeys(s) == collections.OrderedDict.fromkeys(t)

obj = Solution()
print(obj.isSubsequence("aaaaaa","bbaaaa"))