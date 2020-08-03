from typing import *
import unittest

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        """
        Task: traverse the tree and determine if the trees are the same
        Intuition: If I use level order traversal, I may be able to carry this out. But that may be the wrong approach.
                        This may be better suited for a recursive problem.

        Algorithm: 
            - base case is the node is None
            - return if recursive to the left and recursive to the right are equal
        """
        if not p and not q:
            return True
        
        if p.val != q.val:
            return False
        if (p and not q) or (not p and q):
            return False
        return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)


class TestIsSameTree(unittest.TestCase):
    def test_same_tree(self):
        pass

unittest.main(verbosity=2)
