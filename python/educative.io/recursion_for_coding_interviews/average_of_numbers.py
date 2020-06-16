def average(testVariable, currentIndex = 0) : 
	# """
  # Task: implement a recursive function that calculates the average
  #       of the numbers within the array
  # 1. base case is if the current index is the end of the array
  # 2. divide the recursive stack by the number of elements within the array
  # 3. return the curr el + the rest
  # """
	# base case
  if currentIndex == len(testVariable) - 1:
    return testVariable[currentIndex]
  if currentIndex == 0:
    return (testVariable[currentIndex] + average(testVariable, currentIndex + 1)) // len(testVariable)
  return testVariable[currentIndex] + average(testVariable, currentIndex+1)