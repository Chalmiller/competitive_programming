from collections import deque

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
      if not root:
        return []
      # bfs approach
      queue = deque()
      queue.append(root)
      res = []

      while queue:
        curr_length = len(queue)
        curr_level = []

        for _ in range(curr_length):
          curr_el = queue.popleft()

          curr_level.append(curr_el.val)

          if curr_el.left:
            queue.append(curr_el.left)
          if curr_el.right:
            queue.append(curr_el.right)
        res.append(curr_level)
      
      return res
