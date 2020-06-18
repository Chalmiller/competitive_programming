def search_ceiling_of_a_number(arr, key):
  """
  Task: Find the closest number to the key

  Algorithm:
    1. check the boundary position
        if the key is less than the first element, return 0
        if the key is greater than the last element, return -1
    2. else return the index + 1 when start == end

  Time Complexity - O(logn)
  Space - O(1)
  """
  # [1, 3, 8, 10, 15], 12
  start, end = 0, len(arr) - 1
  if key > arr[end]:
    return -1
  
  if key < arr[start]:
    return 0

  while start <= end:
    if start == end:
      return start

    mid = start + (end-start)//2
    if key == arr[mid]:
      return mid
    elif key > arr[mid]:
      low = mid + 1
    else:
      high = mid -1


def main():
  print(search_ceiling_of_a_number([4, 6, 10], 6))
  print(search_ceiling_of_a_number([1, 3, 8, 10, 15], 12))
  print(search_ceiling_of_a_number([4, 6, 10], 17))
  print(search_ceiling_of_a_number([4, 6, 10], -1))


main()