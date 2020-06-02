class TreeNode:
  def __init__(self, key):
    self.data = key
    self.left = None
    self.right = None

def minDepth(root):
  if not root:
    return 0
  
  if not root.left or root.right:
    return 1

  if not root.left:
    return minDepth(root.right) + 1

  if not root.right:
    return minDepth(root.left) + 1

  return min(minDepth(root.left), minDepth(root.right)) + 1