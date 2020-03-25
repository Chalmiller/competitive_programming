# 897: Increasing Order Search Tree

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def increasingBST(self, root: TreeNode, tail = None) -> TreeNode:
        if not root: return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res

    def increasingBST_iterative(self, root: TreeNode) -> TreeNode:
        new = head = TreeNode(0)
        array_stack = []
        while array_stack or root:
            while root:
                array_stack.append(root)
                root = root.left
            root = array_stack.pop()
            new.right = root
            new = new.right
            root = root.right
            new.left = None
        return head.right

