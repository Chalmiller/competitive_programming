from typing import *

class Solution:
    def transpose(self, A: List[List[int]]) -> List[List[int]]:
        # We coul just use zip here, but we will do it manually
        transpose = [[] for _ in range(len(A[0]))]
        for i in range(len(A)):
          for j in range(len(A[0])):
            transpose[j].append(A[i][j])
        return transpose

obj = Solution()
print(obj.transpose([[1,2,3],[4,5,6]]))
