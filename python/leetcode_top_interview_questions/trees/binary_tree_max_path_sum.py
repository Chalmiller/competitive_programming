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
    def maxPathSum(self, root: TreeNode) -> int:
        """
        Task: Return the max path sum in the tree
        Intuition: I had to look at the solution description

        Algorithm:
            - initiate max_sum 
            - implement max_gain(node):
                - if node is null return 0
                - call max_gain on both the left and right subtree
                - check to start a new path or an old path
                - return the max gain the node and one zero of its subtrees could add to the current path
        """
        def max_gain(node):
            global max_sum
            if not node:
                return 0
            
            left_gain = max(max_gain(node.left), 0)
            right_gain = max(max_gain(node.right), 0)

            price_new_path= node.val + left_gain + right_gain

            max_sum = max(max_sum, price_new_path)

            return node.val + max(left_gain, right_gain)
        
        max_sum = -math.inf
        max_gain(root)
        return max_sum

class TestMaxPathSum(unittest.TestCase):
    def test_max_path_sum(self):
        pass

unittest.main(verbosity=2)
