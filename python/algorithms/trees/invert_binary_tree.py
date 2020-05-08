# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque
class Solution:
    def invertTree(self, root: TreeNode) -> TreeNode:
        # queue = deque()
        # queue.append(root)

        # while queue:
        #   curr_length = len(queue)
        #   for _ in range(curr_length):
        #     node = queue.popleft()
        #     if node:
        #       if node.left or node.right:
        #         temp = node.left
        #         node.left = node.right
        #         node.right = temp
        #         queue.append(node.left)
        #         queue.append(node.right)
        # return root            

        if root:
          root.left, right.right = self.invertTree(root.right), self.invertTree(root.left)
          return root