from collections import deque

def inorder_iterative(root):
  """
  Task: Write and inorder dfs traversal algorithm that returns the traversal as a string

  Algorithm:
  1. dfs iterative traversal
  2. append every node to the result string given
  3. return the result string

  Time Complexity - O(n)
  Space - O(1) - since it's just a string we are storing
  """
  result = ""
  if not root:
    return 

  stack = deque()
  count = 0

  while len(stack) != 0 or root != None:
    if root != None:
      stack.append(root)
      root = root.left
      continue
    result += str(stack[-1].data) + " "
    root = stack[-1].right
    stack.pop()
  return str(result)
