# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import *
from collections import deque

class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        queue = deque()
        if root is None:
          return root

        queue.append(root)
        result = []
        while queue:
          curr_length = len(queue)
          current_level = []
          for _ in range(curr_length):
            curr_el = queue.popleft()
            current_level.append(curr_el.val)

            if curr_el.left:
              queue.append(curr_el.left)
            if curr_el.right:
              queue.append(curr_el.right)
            
          result.insert(0, current_level)
        
        return result


