from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {"(" : ")", "{" : "}", "[" : "]"}
        for i in range(len(s)):
          if s[i] == "(" or s[i] == "{" or s[i] == "[":
            stack.append(s[i])
          else:
            curr_el = stack.pop()
            if not s[i] == pairs[curr_el]:
              return False
        return not stack

obj = Solution()
print(obj.isValid("{[]}"))

