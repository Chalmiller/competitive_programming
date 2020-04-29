def findSquare(targetNumber) :
  if targetNumber == 0:
    return 0
  else:
    return findSquare(targetNumber - 1) + (2 * targetNumber) - 1