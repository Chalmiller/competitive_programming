from typing import *
import collections

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: TreeNode) -> int:
      def bfs(node):
        queue = []
        queue.append(root)
        res = []

        while queue:
          curr_level = []
          curr_length = len(queue)

          for _ in range(curr_length):
            el = queue.pop(0)
            if el.val % 2 == 0:
              if el.left:
                if el.left.left:
                  res.append(el.left.left)
                if el.left.right:
                  res.append(el.left.right)
              if el.right:
                if el.right.left:
                  res.append(el.right.left)
                if el.right.right:
                  res.append(el.right.right)
            if el.left:
              queue.append(el.left)
            if el.right:
              queue.append(el.right)
            
        return res
      
      result = bfs(root)
      return sum(result)
           
