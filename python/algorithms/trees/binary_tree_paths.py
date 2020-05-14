from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:
        def dfs(node, res):
          if root:
            res.append(node.val)
            dfs(node.left, res)
            dfs(node.right, res)
          return res

        result = []
        dfs(root, result)
        return result
