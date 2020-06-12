def firstIndex(arr, testVariable, currentIndex) :
  """
  Task: find a target number within an array

  Algorithm:
  1. recursive iterative search through an array
  """
  # base case: 
  # if the current_index == len(arr) - 1, or the last element of the array
  last_el = len(arr)
  if currentIndex == last_el:
    return -1
  
  if arr[currentIndex] == testVariable:
    return currentIndex
  
  return firstIndex(arr, testVariable, currentIndex + 1)
