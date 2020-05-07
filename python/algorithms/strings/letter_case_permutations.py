from typing import *
from collections import deque

class Solution:
    def letterCasePermutation(self, S: str) -> List[str]:
        result = []
        queue = deque()
        queue.append("")
        index = 0
        while queue and index < len(S):
          queue_length = len(queue)
          for _ in range(queue_length):
            curr_perm = queue.popleft()
            if S[index].isalpha():
              lower = curr_perm + S[index]
              upper = curr_perm + S[index].swapcase()
              queue.append(lower)
              queue.append(upper)
            else:
              queue.append(curr_perm + S[index])
          index += 1
        return list(queue)

obj = Solution()
print(obj.letterCasePermutation("C"))
            

