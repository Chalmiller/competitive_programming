from typing import *

class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_string = str(x)
        start, end = 0, len(str(x)) - 1

        while start < end:
          if num_string[start] == num_string[end]:            
            start += 1
            end -= 1
          else:
            return False
        return True

obj = Solution()
print(obj.isPalindrome(10))