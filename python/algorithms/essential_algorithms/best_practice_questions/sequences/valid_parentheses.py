from typing import *

class Solution:
    def isValid(self, s: str) -> bool:
      """
        1. iterate through the array
        2. if open paren, append it to the stack
        3. if close paren, pop from stack and compare
        4. if close paren doesn't match the open paren, return False
        5. if we reach the bottom of the stack, return True
        Note: if we find a closing paren without anything in the stack, we automatically return False
      """ 
      cache = {'(': ')', '{': '}', '[': ']'}
      stack = []
      # "]([)]" - False
      # "()[]{}" - True
      for paren in s:
        if not stack and paren not in cache.keys():
          return False
        elif paren in cache.keys():
          stack.append(paren)
        else:
          top = stack.pop()
          if cache[top] != paren:
            return False
          else:
            continue
      return not stack

obj = Solution()
print(obj.isValid("([])"))


