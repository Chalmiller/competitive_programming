from typing import *

class Solution:
    def repeatedStringMatch(self, A: str, B: str) -> int:
        if A not in B:
          return -1
        orig = A
        while B not in A:
          A = A + A
        print(A)
        return A.count(orig)

obj = Solution()
print(obj.repeatedStringMatch("abcd", "cdabcdab"))