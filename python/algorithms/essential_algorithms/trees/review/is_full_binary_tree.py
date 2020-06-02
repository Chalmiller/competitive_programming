def is_full_tree(root):
  if not root:
    return True

  if not root.left and not root.right:
    return True

  if root.left and root.right:
    return (is_full_tree(root.left) and is_full_tree(root.right))
  
  return False