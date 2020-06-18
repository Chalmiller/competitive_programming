def find_range(arr, key):
  """
  Task: find the range of a given number key, else return [-1,-1]

  Algorithm:
  1. Set up binary search
  2. 
  """
  response = [-1, -1]
  response[0] = binary_search(arr, key, False)
  if response[0] != -1:
    response[1] = binary_search(arr, key, True)
  return response

def binary_search(arr, key, find_max):
  key_index = -1
  start, end = 0, len(arr) - 1

  while start <= end:
    mid = start + (end - start)//2

    if key < arr[mid]:
      end = mid - 1
    elif key > arr[mid]:
      start = mid + 1
    else:
      key_index = mid
      if find_max:
        start = mid + 1
      else:
        end = mid - 1
  return key_index

def main():
  print(find_range([4, 6, 6, 6, 9], 6))
  print(find_range([1, 3, 8, 10, 15], 10))
  print(find_range([1, 3, 8, 10, 15], 12))


main()
