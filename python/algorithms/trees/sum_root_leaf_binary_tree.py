from typing import *

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumRootToLeaf(self, root: TreeNode) -> int:
        def dfs(node, bits, res):
          if node.left == None and node.right == None:
            res[0] += int(bits + str(node.val), 2)
          if node.left:
            dfs(node.left, bits + str(node.val), res)
          if node.right:
            dfs(node.right, bits + str(node.val), res)
        if root == None:
          return 0
        bits, res = '', [0]
        dfs(root, bits, res)
        return res[0]
