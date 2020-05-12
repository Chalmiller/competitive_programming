from typing import *

class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        groups = [1]
        for i in range(1, len(s)):
          if s[i-1] != s[i]:
            groups.append(1)
          else:
            groups[-1] += 1
        print(groups)
        ans = 0
        for i in range(1, len(groups)):
          ans += min(groups[i-1], groups[i])
        return ans

obj = Solution()
print(obj.countBinarySubstrings("00110011"))