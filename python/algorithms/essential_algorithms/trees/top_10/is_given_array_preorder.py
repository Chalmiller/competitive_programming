INT_MIN = -2**32

def canRepresentBST(pre):
  s = []

  root = INT_MIN

  for value in pre:

    if value < root:
      return False

    while (len(s) > 0 and s[-1] < value):
      root = s.pop()

    s.append(value)

  return True