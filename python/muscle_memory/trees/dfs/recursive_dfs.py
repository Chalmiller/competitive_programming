class Node:
  def __init__(self, data):
    self.data = data
    self.left = None
    self.right = None

def recursive_inorder_dfs(root):

  def dfs(node, res):
    if node:
      dfs(node.left, res)
      res.append(node.data)
      dfs(node.right, res)

  res = []
  dfs(root, res)
  return res

def recrusive_preorder_dfs(root):

  def dfs(node, res):
    if node:
      res.append(node.data)
      dfs(node.left, res)
      dfs(node.right, res)

  res = []
  dfs(root, res)
  return res

def recursive_postorder_dfs(root):

  def dfs(node, res):
    if node:
      dfs(node.left, res)
      dfs(node.right, res)
      res.append(node.data)

  res = []
  dfs(root, res)
  return res

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print(recursive_inorder_dfs(root))
print(recursive_postorder_dfs(root))
print(recrusive_preorder_dfs(root))
