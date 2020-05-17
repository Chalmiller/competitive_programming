from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        def dfs(node, res, paths = []):
          if node:
            new_path.append(node.val)
            if not node.left and not node.right:
              res.append(new_path)
            dfs(node.left, res, new_path)
            dfs(node.right, res, new_path)
          return res
        
        response = []
        dfs