def recursiveLength(testVariable):
    if len(testVariable) == 1:
      return 1
    else:
      return recursiveLength(testVariable[1:]) + 1
print(recursiveLength("Educative"))

  