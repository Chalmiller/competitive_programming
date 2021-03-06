# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def trimBST(self, root: TreeNode, L: int, R: int) -> TreeNode:
      if not root:
        return None
      elif root.val < L:
        return self.trimBST(root.right, L, R)
      elif root.val > R:
        return self.trimBST(root.left, L, R)  
      else:
        root.left, root.right = self.trimBST(root.left), self.trimBST(root.right)
        return root
      
      
          