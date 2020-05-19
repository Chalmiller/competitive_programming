from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        def equals(x, y):
          if x == None and y == None:
            return True
          if x == None or y == None:
            return False
          return x.val == y.val and equals(x.left, y.left) and equals(x.right, y.right)

        def traverse(s, t):
          return s != None and (equals(s, t) or traverse(s.left, t) or traverse(s.right, t))
        
        return traverse(s, t)