import math

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        """
        Task: 
          - return boolean if the tree is a valid binary search tree
        Intuition:
          - left will be less than the node and right will be more than the node

        Algorithm:
          - we can use dfs on the tree
          - if left is less than, run recursion on the left 
          - if right is greater than node, run recursion on the right side
          - return if either of those conditions don't hold up
        """

        def helper(node, lower = -math.inf, upper = math.inf):
          if not node:
            return True
          val = node.val
          if val <= lower or val >= upper:
            return False
          
          if not helper(node.right, val, upper):
            return False
          if not helper(node.left, lower, val):
            return False
          return True

        return helper(root)

        # stack, inorder = [], 0

        # while True:
        #   while root:
        #     stack.append(root.val)
        #     root = root.left
          
        #   root = stack.pop()

        #   if root.val <= inorder:
        #     return False
        #   inorder = root.val
        #   root = root.right

        # return True
