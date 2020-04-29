def isPalindrome(testVariable) :
  if len(testVariable) <= 1:
    return True
  else:
    length = len(testVariable)
    if testVariable[0] == testVariable[length - 1]:
      return isPalindrome(testVariable[1:length - 1])
  return False