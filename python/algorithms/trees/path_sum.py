from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        def dfs(node, _sum):
          if node:
            if node.val == _sum:
              return True
            dfs(node.left, _sum - node.left)
            dfs(node.right, _sum - node.right)
            return False

        return dfs(root, sum)