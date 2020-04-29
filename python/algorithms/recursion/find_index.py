def firstIndex(arr, testVariable, currentIndex):
  if currentIndex > len(arr) - 1:
    return -1
  elif arr[currentIndex] == testVariable:
    return currentIndex
  else:
    return firstIndex(arr, testVariable, currentIndex + 1)

print(firstIndex([9, 8, 1, 8, 1, 7], 1, 0))