def isPalindrome(testVariable) :
  """
  Task: use recursion to determine if a string is a palindrome

  1. base case is if the length of the test variable is 1
  2. return the string with the edges clipped off if the edges are equal
  """
  # base case 1
  if len(testVariable) <= 1:
    return True
  # base case 2
  length = len(testVariable)
  if testVariable[0] == testVariable[length-1]:
    return isPalindrome(testVariable[1: length-1])

  return False