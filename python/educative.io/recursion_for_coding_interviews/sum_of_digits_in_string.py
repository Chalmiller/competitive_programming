def sumDigits(testVariable):
  """
  Task: convert a string decimal into the sum of its respective int digits

  1. base case is the length of the string is 0
  2. return the int conversion of of the first digit in the string plus the rest of the string
  """
  # base case
  if not testVariable:
    return 0
  return int(testVariable[0]) + sumDigits(testVariable[1:])