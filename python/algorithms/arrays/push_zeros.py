def move_zeros(array):
    zeros = []
    nums = []

    for el in array:
      if el is int() or el is float():
        print(el)
        if el > 0:
          nums.append(el)
        else:
          zeros.append(el)
      else:
        nums.append(el)
    return nums + zeros
    
print(move_zeros([9, 0.0, 9, 1, 2, 1, 1, 0.0, 3, 1, 9, 9, 0, 0, 0, 0, 0, 0, 0, 0]))