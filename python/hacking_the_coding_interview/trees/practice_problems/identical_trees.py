

def are_identical(root1, root2):
  """
  Task: traverse the trees to find if they are identical or not

  Algorithm:
  1. implement a dfs algorithm
  2. iterate through both trees simultaneously comparing their nodes each step
  3. if ever the nodes don't match return False
  4. else return True

  Time Complexity - O(n)
  Space - O(1) since we aren't holding any of the values
  """
  
  if not root1 and not root2:
    return True
  if root1 and root2:
    return (root1.data == root2.data and 
    are_identical(root1.left, root2.left) 
    and are_identical(root1.right, root2.right))

arr1 = [100,50,200,25,125,350]
arr2 = [1,2,10,50,180,199]
root1 = create_BST(arr1)
display_level_order(root1)
root2 = create_BST(arr2)

display_level_order(root2)
if(are_identical(root1, root2)):
  print("The trees are identical")
else:
  print("The trees are not identical")
        