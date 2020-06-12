def findSquare(targetNumber, exponent):
  # base case when the exponent is 1
  if exponent == 1:
    return targetNumber
  # return the target number times itself
  return findSquare(targetNumber, exponent - 1) * targetNumber

print(findSquare(5, 2))
