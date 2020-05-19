from typing import *
from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def convertBST(self, root: TreeNode) -> TreeNode:
        total = 0

        stack = []
        node = root
        while stack or node is not None:

          while node is not None:
            stack.append(node.val)
            node = node.right
          
          node = stack.pop()
          total += node.val
          node.val = total

          node = node.left
          
        return root







          
