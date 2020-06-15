def recursiveLength(testVariable): 
	# """
  # Task: Implement a recursive function that returns the length of a string

  # 1. base case would be the string is empty
  # 2. return 1 + the rest of the string recursively
  # """

  if not testVariable:
    return ""
  return 1 + recursiveLength(testVariable[1:])