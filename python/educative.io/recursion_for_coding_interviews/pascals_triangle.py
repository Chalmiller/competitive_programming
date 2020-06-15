def printPascal(testVariable):
  # base case is if the testVariable is 1
  if testVariable == 0:
    return [1]
  else:
    # we will construct the pascal triangle level by iterating from 1 -> testvariable
    # and adding i + i
    line = [1] 
    previous_line = printPascal(testVariable - 1)
    for i in range(len(previous_line)-1):
      line.append(previous_line[i] + previous_line[i+1])
    line += [1]
  return line

print(printPascal(4))
