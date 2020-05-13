from typing import *
import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getMinimumDifference(self, root: TreeNode) -> int:

        def dfs(node, res):
          if node:
            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        result = []
        dfs(root, result)
        result.sort()
        return abs(result[0] - result[1])


