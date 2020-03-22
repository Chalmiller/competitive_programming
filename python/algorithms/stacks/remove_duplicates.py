from typing import *

class Solution:
    def removeDuplicates(self, S: str) -> str:
        array_stack = []
        array_stack.append("#")

        for i, el in enumerate(S):
            if el == array_stack[-1]:
                array_stack.pop()
            else:
                array_stack.append(el)
        return "".join(array_stack[1:])

test_string = "aaaaa"
obj = Solution()
obj.removeDuplicates(test_string)