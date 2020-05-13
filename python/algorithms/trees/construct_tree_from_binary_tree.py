from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, t: TreeNode) -> str:
        def preorder_dfs(node, res):
          if node:
            res.append((node.val))
            response.append('(')
            preorder_dfs(node.left, res)
            preorder_dfs(node.right, res)
            response.append(')')
        
        response = []
        preorder_dfs(t, response)
        valid_paren = "".join([str(el) for el in response])
        print(valid_paren)
        return response
