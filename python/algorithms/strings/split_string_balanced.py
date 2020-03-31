# 1221: Split a String in Balanced Strings
from typing import *

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        # Stack Implementation
        stack = [s[0]]
        count = 0

        for index in range(1, len(s)):
            if not stack:
                stack.append(s[index])
            else:
                if stack[len(stack) - 1] == s[index]:
                    stack.append(s[index])
                else:
                    stack.pop()
                    if not stack:
                        count += 1
        return count
        # other implementation
        res = cnt = 0
        for c in s:
            cnt += 1 if c == 'L' else -1
            if cnt == 0:
                res += 1
        return res

obj = Solution()
num = obj.balancedStringSplit("RLRRRLLRLL")
print(num)