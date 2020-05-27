from typing import *

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
      if not needle:
        return 0
      try:
        index_of = haystack.index(needle)
        return index_of
      except:
        # sliding window
        sub = len(needle)
        for i in range(0, len(haystack) - sub):
          if haystack[i:i+sub] == needle:
            return i
        return -1
        

obj = Solution()
print(obj.strStr("hello", "ll"))
