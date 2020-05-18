from typing import *

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
      index = 0

      while index < len(s):
        s = list(s[:index]) + list(reversed(s[index:index+k])) + list(s[index + k:])
        index += 2*k
      return "".join(s)

obj = Solution()
print(obj.reverseStr("abcdefg", 2))