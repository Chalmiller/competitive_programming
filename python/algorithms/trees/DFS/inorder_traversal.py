# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
      result = []
      self.dfs(root, result)
      return result
        
    def dfs(self, node, result):
      if node:
        self.dfs(node.left, result)
        result.append(node.val)
        self.dfs(node.right, result)