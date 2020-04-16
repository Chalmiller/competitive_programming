# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import *
from collections import deque

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        queue = deque()
        zig_zag = True

        result = []

        queue.append(root)
        while queue:
          curr_level = []
          q_length = len(queue)

          for _ in range(q_length):
            curr_el = queue.popleft()
            curr_level.append(curr_el.val)
            
            if curr_el.left:
              queue.append(curr_el.left)
            if curr_el.right:
              queue.append(curr_el.right)
          if zig_zag:
            result.append(curr_level)
          else:
            result.append(curr_level[::-1])
          
          zig_zag = not zig_zag
        return result