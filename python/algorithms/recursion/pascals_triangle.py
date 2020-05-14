def printPascal(testVariable) :
  if testVariable == 0:
    return [1]
  else:
    line = [1]

    previous_line = printPascal(testVariable - 1)
    for i in range(len(previous_line) - 1):
      line.append(previous_line[i] + previous_line[i + 1])
    line += [1]
  return line

print(printPascal(5))