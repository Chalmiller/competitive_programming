from typing import *
import unittest
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
        Task: Verify that the binary search tree is a valid BST
        Intuition: Preorder traversal will append the nodes in least to greatest order.

        Algorithm:
          - Do in order traversal of the tree and append each node to a closure list
          - iterate through that array and check that every element is in place
        """

        # def inorder_dfs(node, inorder_nodes):
        #   if not node:
        #     return 
        #   else:
        #     inorder_dfs(node.left, inorder_nodes)
        #     inorder_nodes.append(node.val)
        #     inorder_dfs(node.right, inorder_nodes)
        
        # inorder_list = []
        # inorder_dfs(root, inorder_list)

        # for i in range(len(inorder_list) - 1):
        #   if inorder_list[i] > inorder_list[i+1]:
        #     return False

        # return True

        stack = []
        inorder = -math.inf

        while stack or root:
          while root:
            stack.append(root)
            root = root.left

          root = stack.pop()

          if root.val <= inorder:
            return False
          inorder = root.val
          root = root.right
        return True


class TestIsValidBST(unittest.TestCase):

    def test_valid_tree(self):
      pass

unittest.main(verbosity=2)
