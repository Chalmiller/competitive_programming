# 921: Minimum Add to Make Parentheses Valid
from typing import *

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        array_stack = []
        count = 0

        for i, el in enumerate(S):
            if el == '(': 
                array_stack.append(el)
            elif el == ')': 
                if not array_stack:
                    count += 1
                    continue
                array_stack.pop()
            
        return count + len(array_stack)

test_string = "()))(("
obj = Solution()
obj.minAddToMakeValid(test_string)
            