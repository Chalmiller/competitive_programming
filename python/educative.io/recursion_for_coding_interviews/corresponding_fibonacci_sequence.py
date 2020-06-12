def fibonacci(testVariable):
  if testVariable <=1:
    return testVariable
  return fibonacci(testVariable - 1) + fibonacci(testVariable - 2)
