# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import *
from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        queue = deque()
        result = []

        queue.append(root)

        while queue:
          q_length = len(queue)
          curr_level = []

          for _ in range(q_length):
            curr_el = queue.popleft()
            queue.append(curr_el.val)

            if curr_el.left:
              curr_level.append(curr_el.left)
            if curr_el.right:
              curr_level.append(curr_el.right)

          if len(curr_level) % 2 == 0:
            if curr_level.reverse() != curr_level:
              return False
          else:
            return False
        return True
