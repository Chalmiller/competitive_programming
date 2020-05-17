from typing import *

class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        for i in range(0, len(s), 2*k):
          s = "".join(list(reversed(s[i:i+k])))
          print(s) 

obj = Solution()
print(obj.reverseStr("abcdefg", 2))