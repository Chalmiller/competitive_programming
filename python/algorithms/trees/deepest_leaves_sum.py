from typing import *
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:
        def bfs(node):
          queue = collections.deque()
          queue.append(node)
          res = []

          while queue:
            curr_level = []
            curr_length = len(queue)
            for _ in range(curr_length):
              curr_el = queue.popleft()
              curr_level.append()
              if curr_el.left:
                queue.append(curr_el.left)
              if curr_el.right:
                queue.append(curr_el.right)
            res.append(curr_level)
          return res

        levels = bfs(root)
        return sum(levels[-1])
