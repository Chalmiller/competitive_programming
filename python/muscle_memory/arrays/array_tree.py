def solution(arr):
  left, right = 0, 0
  i = 1 
  while i < len(arr):
    left += arr[i]
    i = 2*i + 1
    if i >= len(arr):
      break
    left += arr[i]
    i = 2*i + 1

  i = 2 
  while i < len(arr):
    right += arr[i]
    i = 2*i + 1
    if i >= len(arr):
      break
    right += arr[i]
    i = 2*i + 1
  if right == left:
    return ""
  elif right > left:
    return "Right"
  else:
    return "Left"