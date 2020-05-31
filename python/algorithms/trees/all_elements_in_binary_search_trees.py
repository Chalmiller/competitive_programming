from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getAllElements(self, root1: TreeNode, root2: TreeNode) -> List[int]:
        self.vals = []

        def dfs(node):
          if not node:
            return None
          self.vals.append(node.val)
          dfs(node.left)
          dfs(node.right)
          return node

        dfs(root1)
        dfs(root2)
        self.vals.sort()
        return self.vals