class Node: 
    def __init__(self , key): 
        self.data = key  
        self.left = None
        self.right = None

def minDepth(root):
  if not root:
    return 0

  if not root.left and not root.right:
    return 1

  if not root.left:
    return minDepth(root.right)
  
  if not root.right:
    return minDepth(root.left)

  return min(minDepth(root.left), minDepth(root.right)) + 1