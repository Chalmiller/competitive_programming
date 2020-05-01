def shortest_window_sort(arr):
  sort_reference = sorted(arr)
  start, end = 0, len(arr) - 1

  while start < end:
    while arr[start] == sort_reference[start]:
      start += 1
    while arr[end] == sort_reference[end]:
      end -= 1
    
    return len(arr[end:start])

  return -1