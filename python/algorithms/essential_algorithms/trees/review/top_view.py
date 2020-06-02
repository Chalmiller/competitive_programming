class newNode:  
  # Construct to create a newNode  
  def __init__(self, key):  
    self.data = key 
    self.left = None
    self.right = None
    self.hd = 0

def top_view(root):
  if not root:
    return 

  q = []
  m = dict()
  hd = 0
  root.hd = hd

  q.append(root)
  while (len(q)):
    root = q.pop(0)
    hd = root.hd

    if hd not in m:
      m[hd] = root.data
    if (root.left):
      root.left.hd = hd - 1
      q.append(root.left)
    if root.right:
      root.right.hd = hd + 1
      q.append(root.right)

    
  
  for i in sorted(m):
    print(m[i], end="")