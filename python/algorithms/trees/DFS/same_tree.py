# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
      if q.left and p.left:
        self.isSameTree(p.left, q.left)
      if q.right and p.right:
        self.isSameTree(p.right, q.right)
      return p == q