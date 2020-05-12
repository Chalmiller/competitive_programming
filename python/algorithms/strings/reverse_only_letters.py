from typing import *

class Solution:
    def reverseOnlyLetters(self, S: str) -> str:
        prev_char = 0
        good_string = ""
        response_string = ""
        for i, char in enumerate(S):
          if char.isalpha():
            good_string = good_string + char
        good_string = list(good_string[::-1])
        
        for char in S:
          if char.isalpha():
            response_string = response_string + good_string.pop(0)
          else:
            response_string = response_string + char
        return response_string


obj = Solution()
print(obj.reverseOnlyLetters("Test1ng-Leet=code-Q!"))

