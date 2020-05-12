from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:
        def dfs(node, res):
          if node:
            res.append(node.val)
            dfs(node.left, res)
            dfs(node.right, res)
        res = []
        if len(res) == 1 and res[0] != k:
          return False
        dfs(root, res)
        res.sort()
        print(res)
        low, high = 0, len(res) - 1
        while low <= high:
          curr_sum = res[low] + res[high]
          if curr_sum > k:
            high -= 1
          elif curr_sum < k:
            low += 1
          else:
            return True
        return False
