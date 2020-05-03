def sumDigits(testVariable):
    if len(testVariable) == 1:
      return int(testVariable)
    else:
      return int(testVariable[0]) + sumDigits(testVariable[1:])

      