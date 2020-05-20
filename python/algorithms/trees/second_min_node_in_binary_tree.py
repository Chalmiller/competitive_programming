from typing import *
import heapq

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        def dfs(node,res):
          if node:
            res.append(node.val)
            dfs(node.left, res)
            dfs(node.right, res)
          return res
        
        result = []
        dfs(root, result)
        smallest = heapq.nsmallest(2, list(set(result)))[1] if len(set(result)) > 1 else -1
        return smallest