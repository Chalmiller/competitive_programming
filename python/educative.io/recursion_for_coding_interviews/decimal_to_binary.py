def decimalToBinary(testVariable) :
  """
  Task: Convert and return the decimal number as a binary string

  Algorithm:
  1. for each recursive call we want to divide the testVariable by 2 and append 
    a 1 to the result
  """
  if testVariable <= 1:
    return str(testVariable)
  else:
    remainder = str(testVariable % 2)
    return "" + decimalToBinary(testVariable//2) + remainder

print(decimalToBinary(11))
  