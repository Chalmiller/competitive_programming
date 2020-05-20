from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: TreeNode) -> bool:
        levels = []

        def bfs(node, leaf_depth):
          if node:
            leaf_depth += 1
            if not node.left and not node.right:
              levels.append(leaf_depth)
            bfs(node.left, leaf_depth)
            bfs(node.right, leaf_depth)
          return leaf_depth

        bfs(root, 0)
        print(levels)