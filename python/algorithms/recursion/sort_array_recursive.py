def sort(testVariable, length):
    if length <= 1:
      return
    
    sort(testVariable, length - 1)

    last_element = testVariable[length - 1]
    temp = length - 2

    while (temp >= 0 and testVariable[temp] > last_element):
      testVariable[temp + 1] = testVariable[temp]
      temp -= 1
    
    testVariable[temp + 1] = last_element