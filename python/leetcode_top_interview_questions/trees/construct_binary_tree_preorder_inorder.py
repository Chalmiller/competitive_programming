from typing import *
import unittest

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """
        Task: Recreate a binary tree from a preorder and inorder traversal
        Intuition: It seems like this is a good functional programming assignment

        Algorithm:
            - maybe if I build a level order representation, I could navigate through that
            - 2i+1 and 2i+2
        """
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]

        i = 1
        j = 0

        while i < len(preorder):
            node = TreeNode(preorder[i])
            if stack[-1].val != inorder[j]:
                stack[-1].left = node
            else:
                while stack and stack[-1].val == inorder[j]:
                    last_node = stack.pop()
                    j += 1
                last_node.right = node
            stack.append(node)
            i += 1
        return root


class TestBuildTree(unittest.TestCase):
    def test_building_tree(self):
        pass

unittest.main(verbosity=2)
