def gcd(testVariable1, testVariable2) :
  """
  Task: Find and return the greatest common divisor of the two input numbers

  Algorithm:
  1. subtract the test variables from eachother and return the recursive function until they match
  """
  if testVariable1 == testVariable2:
    return testVariable1
  if testVariable1 > testVariable2:
    return gcd(testVariable1 - testVariable2, testVariable2)
  return gcd(testVariable1, testVariable2 - testVariable1)