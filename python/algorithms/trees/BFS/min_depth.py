# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import *
from collections import deque

class Solution:
  def minDepth(self, root: TreeNode) -> int:
    if not root:
      return 0
    queue = deque()
    min_depth = 1
    queue.append(root)

    while queue:
      q_length = len(queue)
      curr_level = []
      for _ in range(q_length):
        curr_el = queue.popleft()
        curr_level.append(curr_level)

        if not curr_el.left or not curr_el.right:
          return min_depth
        else:
          queue.append(curr_el.left)
          queue.append(curr_el.right)
      min_depth += 1
    return min_depth
      
