import math


class ArrayReader:

  def __init__(self, arr):
    self.arr = arr

  def get(self, index):
    if index >= len(self.arr):
      return math.inf
    return self.arr[index]


def search_in_infinite_array(reader, key):
  """
  Task: return the index of the key in the array

  Algorithm:
  1. binary search
  2. increase bound size exponentially as we loop
  """
  start, end = 0, 1
  while reader.get(end) < key:
    new_start = end + 1
    end += (end - start + 1) * 2
    start = new_start

  return binary_search(start, end, reader, key)

def binary_search(start, end, reader, key):
  
  while start <= end:
    mid = start + (end - start)//2

    if key > reader.get(mid):
      start = mid + 1
    elif key < reader.get(mid):
      end = mid - 1
    else:
      return mid

  return -1
  

def main():
  reader = ArrayReader([4, 6, 8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30])
  print(search_in_infinite_array(reader, 16))
  print(search_in_infinite_array(reader, 11))
  reader = ArrayReader([1, 3, 8, 10, 15])
  print(search_in_infinite_array(reader, 15))
  print(search_in_infinite_array(reader, 200))


main()