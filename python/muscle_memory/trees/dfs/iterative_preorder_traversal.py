class Node:

  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def iterative_preorder(root):

  if root is None:
    return

  stack = []
  stack.append(root)

  while stack:
    node = stack.pop()

    print(node)
    if node.right is not None:
      stack.append(node.right)
    if node.left is not None:
      stack.append(node.left)

root = Node(10) 
root.left = Node(20) 
root.right = Node(30) 
root.left.left = Node(40) 
root.left.left.left = Node(70) 
root.left.right = Node(50) 
root.right.left = Node(60) 
root.left.left.right = Node(80) 
  
iterative_preorder(root)   