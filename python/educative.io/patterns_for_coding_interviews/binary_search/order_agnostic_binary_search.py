def binary_search(arr, key):
  # """
  # Task: return the index of the item if it is present, otherwise -1

  # Algorithm:
  # 1. sort the array
  # 2. perform binary search
  # 3. return index of element
  # """
  low, high = 0, len(arr) - 1
  ascending = arr[low] < arr[high]

  # [1, 2, 3, 4, 5, 6, 7], key = 5
  while low <= high:
    mid = low + (high-low)//2
    if arr[mid] == key:
        return mid

    if ascending:
      if arr[mid] > key:
        high = mid - 1
      else:
        low = mid + 1
    else:
      if arr[mid] < key:
        high = mid - 1
      else:
        low = mid + 1
  return -1


def main():
  print(binary_search([4, 6, 10], 10))
  print(binary_search([1, 2, 3, 4, 5, 6, 7], 5))
  print(binary_search([10, 6, 4], 10))
  print(binary_search([10, 6, 4], 4))


main()