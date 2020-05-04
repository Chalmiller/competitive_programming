def search_rotated_array(arr, key):
  start, end = 0, len(arr) - 1
  while start <= end:
    mid = start + (end - start) // 2
    if arr[mid] == key:
      return mid
    
    if arr[start] <= arr[mid]:
      if key >= arr[start] and key < arr[mid]:
        end = mid - 1
      else:
        start = mid + 1
    else:
      if key > arr[mid] and key <= arr[end]:
        start = mid + 1
      else:
        end = mid - 1
