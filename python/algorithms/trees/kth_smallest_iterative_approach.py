from typing import *
import collections

class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
      curr = root
      stack = collections.deque()
      count = 0

      while True:
        while curr:
          stack.append(curr)
          curr = curr.left
        
        if stack:
          curr = stack.pop()
          count += 1
          if count == k:
            return curr.val
          curr = curr.right
        else:
          return -1