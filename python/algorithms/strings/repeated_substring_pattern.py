from typing import *

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        start = 1

        while start < len(s) + 1//2:
          substring = s[:start]

          while len(substring) <= len(s):
            print(substring)
            if substring == s:
              return True
            else:
              substring = substring + s[:start]
          start += 1

        return False

obj = Solution()
print(obj.repeatedSubstringPattern("abcabcabcabc"))
