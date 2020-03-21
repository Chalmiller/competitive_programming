# 1021 - Remove Outermost Parentheses
from typing import *

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        cnt=0
        strlist = []
        ii=0
        for ind, ch in enumerate(S):
            if ch=='(': cnt+=1
            if ch==')': cnt-=1  
            if cnt==0:
                strlist.append(S[ii+1:ind])
                ii = ind+1
        print("".join(strlist))
        return "".join(strlist) 

test_string = "(()())(())(()(()))"
obj = Solution()
obj.removeOuterParentheses(test_string)
