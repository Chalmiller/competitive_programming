from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        queue = deque()
        queue.append(root)
        result = []
        while queue:
          curr_level = []
          curr_length = len(queue)
          for _ in range(curr_length):
            curr_el = queue.popleft()
            curr_level.append(curr_el)
            if curr_el.left:
              queue.append(curr_el.left)
            if curr_el.right:
              queue.append(curr_el.right)
          result.append(sum(curr_level)/len(curr_level))
        return result