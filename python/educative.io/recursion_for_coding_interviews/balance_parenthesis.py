def balanced(testVariable, startIndex = 0, currentIndex = 0) :
  """
  Task: write a recursive function which returns whether an array contains balanced parentheses

  Algorithm:
  1. base case will be when the array is down to 2 elements
  2. return the edges clipped off if the two indices are not equal
  """
  # base case
  if startIndex == len(testVariable):
    return currentIndex == 0

  if currentIndex < 0:
    return False
  
  if testVariable[startIndex] == "(":
    return balanced(testVariable, startIndex + 1, currentIndex + 1)

  elif testVariable[startIndex] == ")":
    return balanced(testVariable, startIndex + 1, currentIndex - 1)
  