class Node:

  def __init__(self,data):
    self.data = data
    self.left = None
    self.right = None
    

def peek(stack):
  if stack:
    return stack[-1]
  return None

def iterative_postorder(root):
  ans = []
  if root is None:
    return
  
  stack = []

  while True:
    while root:
      if root.right is not None:
        stack.append(root.right)
      stack.append(root)

      root = root.left

    root = stack.pop()

    if root.right is not None and peek(stack) == root.right:
      stack.pop()
      stack.append(root)
      root = root.right

    else:
      ans.append(root.data)
      root = None
    if stack:
      break
