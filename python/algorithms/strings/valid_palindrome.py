from typing import *

class Solution:
    def isPalindrome(self, s: str) -> bool:
        munge_input = "".join(char.lower() for char in s if char.isalnum())
        if len(munge_input) < 2:
          return True

        i, j = 0, len(munge_input) - 1

        while i <= j:
          print(munge_input[i], munge_input[j])
          if munge_input[i] != munge_input[j]:
            return False
          i += 1
          j -= 1
        return True

obj = Solution()
print(obj.isPalindrome("0P"))