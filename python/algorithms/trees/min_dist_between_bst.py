from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def minDiffInBST(self, root: TreeNode) -> int:
        def inorder_dfs(node, res):
          if node:
            res.append(node.val)
            inorder_dfs(node.left, res)
            inorder_dfs(node.right, res)
        
        result = []
        inorder_dfs(root, result)
        result.sort()
        return abs(result[0] - result[1])