class Node:  
    def __init__(self, data):  
        self.data = data  
        self.left = self.right = None

def remove_short_path_nodes_util(root, level, k):

  if not root:
    return None

  root.left = remove_short_path_nodes_util(root.left, level + 1, k)
  root.right = remove_short_path_nodes_util(root.right, level + 1, k)

  if not root.left and not root.right and level < k:
    return None

  return root

def remove_short_path_nodes(root, k):
  path_length = 0
  return remove_short_path_nodes_util(root, 1, k)