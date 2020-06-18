def search_min_diff_element(arr, key):
  """
  Task: Find the element with the least difference from the key

  Algorithm:
    1. take the binary search and find the element or nearest element
    2. return the min(end - key, (start - 1) - key)
  """
  start, end = 0, len(arr) - 1
  if key >= arr[end]:
    return arr[end]

  while start <= end:
    mid = start + (end - start)//2

    if key > arr[mid]:
      start = mid + 1
    elif key < arr[mid]:
      end = mid - 1
    else:
      return arr[mid]
  low = abs(arr[start] - key)
  high = abs(arr[end] - key)
  return min(low, high)


def main():
  print(search_min_diff_element([4, 6, 10], 7))
  print(search_min_diff_element([4, 6, 10], 4))
  print(search_min_diff_element([1, 3, 8, 10, 15], 12))
  print(search_min_diff_element([4, 6, 10], 17))


main()