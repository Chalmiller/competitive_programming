from typing import *

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        p, children = [cloned], []

        while p:
          for x in p:
            if x.val == target.val:
              return x
            if x.left:
              children.append(x.left)
            if x.right:
              children.append(x.right)
          p, children = children, []
        return None
              