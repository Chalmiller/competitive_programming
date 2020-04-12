# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def diameterOfBinaryTree(self, root: TreeNode) -> int:
      def height(node):
        if node is None:
          return None
        
        return 1 + max(height(node.left), height(node.right))
        
      if root is None:
        return 0
      
      lheight = height(root.left)
      rheight = height(root.right)

      ldiameter = self.diameterOfBinaryTree(root.left)
      rdiameter = self.diameterOfBinaryTree(root.right)

      return max(lheight + rheight, max(ldiameter, rdiameter))
      

        
