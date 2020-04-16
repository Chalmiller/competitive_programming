# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import *
from collections import deque

class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque()

        if root is None:
          return root

        queue.append(root)
        result = []
        while queue:
          q_length = len(queue)
          curr_level = []
          for _ in range(q_length):
            curr_el = queue.popleft()
            curr_level.append(curr_el.val)

            if curr_el.left:
              queue.append(curr_el.left)
            if curr_el.right:
              queue.append(curr_el.right)

          result.append(curr_level)
        return result