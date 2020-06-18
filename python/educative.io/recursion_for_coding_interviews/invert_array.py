def reverse(array):
  # base case
  if not array:
    return 
  elif len(array) == 1:
    return array
  return array[-1] + reverse(array[:-1])