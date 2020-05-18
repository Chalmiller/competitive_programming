from typing import *
import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        target = round(target)
        def dfs(node, target, res):
          if node:
            res.append((abs(node.val - target), node.val))
            dfs(node.left, target, res)
            dfs(node.right, target, res)
        
        result = []
        dfs(root, target, result)
        result = sorted(result, key=lambda x: x[0])
        return result[0][1]

          
        

        