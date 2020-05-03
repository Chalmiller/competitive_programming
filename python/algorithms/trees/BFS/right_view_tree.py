from __future__ import print_function
from collections import deque


class TreeNode:
  def __init__(self, val):
    self.val = val
    self.left, self.right = None, None


def tree_right_view(root):
  result = []
  
  queue = deque()
  queue.append(root)

  while queue:
    level_size = len(queue)
    curr_level = []
    for _ in range(level_size):
      curr_el = queue.popleft()

      curr_level.append(curr_el.val)

      if curr_el.left:
        queue.append(curr_el.left)
      if curr_el.right:
        queue.append(curr_el.right)


  return result


def main():
  root = TreeNode(12)
  root.left = TreeNode(7)
  root.right = TreeNode(1)
  root.left.left = TreeNode(9)
  root.right.left = TreeNode(10)
  root.right.right = TreeNode(5)
  root.left.left.left = TreeNode(3)
  result = tree_right_view(root)
  print("Tree right view: ")
  for node in result:
    print(str(node.val) + " ", end='')


main()
