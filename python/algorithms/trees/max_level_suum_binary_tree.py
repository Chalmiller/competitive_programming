# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
from typing import *
import math

class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:
        queue = deque()
        queue.append(root)
        sum_results = []

        while queue:
          curr_level = []
          curr_length = len(queue)

          for _ in range(curr_length):
            curr_el = queue.popleft()
            curr_level.append(curr_el.val)
            if curr_el.left:
              queue.append(curr_el.left)
            if curr_el.right:
              queue.append(curr_el.right)
          sum_results.append(sum(curr_level))
        _max = max(sum_results) 

        return (sum_results.index(_max) + 1)
          
