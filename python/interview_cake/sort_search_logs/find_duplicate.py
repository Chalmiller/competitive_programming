import unittest


def find_repeat(numbers):

    # Find a number that appears more than once
    def merge_sort(array):
        if len(array) > 1:
            mid = len(array)//2
            left, right = array[:mid], array[mid:]
            merge_sort(left)
            merge_sort(right)

            i, j, k = 0, 0, 0

            while i < len(left) and j < len(right):
              curr_left = left[i]
              curr_right = right[j]

              if curr_left <= curr_right:
                array[k] = curr_left
                i += 1  
              elif curr_left > curr_right:
                array[k] = curr_right
                j += 1
              k += 1
            
            while i < len(left) - 1:
              array[k] = left[i]
              i += 1
              k += 1

            while j < len(right) - 1:
              array[k] = right[j]
              j += 1
              k += 1
    
    merge_sort(numbers)
    print(numbers)
    for i in range(len(numbers) - 1):
      if numbers[i] == numbers[i+1]:
        return numbers[i]

    return 0


# Tests

class Test(unittest.TestCase):

    def test_just_the_repeated_number(self):
        actual = find_repeat([1, 1])
        expected = 1
        self.assertEqual(actual, expected)

    def test_short_list(self):
        actual = find_repeat([1, 2, 3, 2])
        expected = 2
        self.assertEqual(actual, expected)

    def test_medium_list(self):
        actual = find_repeat([1, 2, 5, 5, 5, 5])
        expected = 5
        self.assertEqual(actual, expected)

    def test_long_list(self):
        actual = find_repeat([4, 1, 4, 8, 3, 2, 7, 6, 5])
        expected = 4
        self.assertEqual(actual, expected)


unittest.main(verbosity=2)