def search_next_letter(letters, key):
  """
  Task: find the smallest letter in an array greater than a key
  Assumptions: 
    - the array is circular
    - if the key is in the array, the next letter shoudl be returned
    - if the key is greater than or equal to the last element, return the first
    - if the key is not in the array, return the next largest letter to it in the array

  Algorithm:
  1. modified binary search is the primary approach
  2. 
  """
  # ['a', 'c', 'f', 'h'], 'b'
  start, end = 0, len(letters) -1
  if key >= letters[end] or key < letters[start]:
    return letters[start]

  while start <= end:
    mid = start + (end - start)//2

    if key == letters[mid]:
      return letters[mid+1]
    elif key > letters[mid]:
      start = mid + 1
    else:
      end = mid - 1

  return letters[start+1]


def main():
  print(search_next_letter(['a', 'c', 'f', 'h'], 'f'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'b'))
  print(search_next_letter(['a', 'c', 'f', 'h'], 'm'))


main()