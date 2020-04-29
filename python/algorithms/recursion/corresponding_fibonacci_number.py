def fibonacci(testVariable) :
    if testVariable == 0:
      return 0
    elif testVariable == 1:
      return 1
    else:
      return fibonacci(testVariable - 2) + fibonacci(testVariable - 1)

print(fibonacci(7))