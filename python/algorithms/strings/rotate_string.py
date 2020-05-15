from typing import *

class Solution:
    def rotateString(self, A: str, B: str) -> bool:
        max_num_rotations = len(A)
        count = 0
        if not A or not B:
          return False
        while count < max_num_rotations:
          print(A, B)
          if A == B:
            return True
          else:
            A = A[1:] + A[:1]
            print(A)
          count += 1
        return False

obj = Solution()
print(obj.rotateString('abcde', 'abced'))