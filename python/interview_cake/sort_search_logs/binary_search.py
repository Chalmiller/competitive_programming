import unittest


def contains(ordered_list, number):

    """
    Task: This is a pretty straight forward binary search question
    Intuition: Again, just binary search here

    Algorithm:
      1. Binary Search
      2. return False if not found

    Time Complexity - O(logn)
    Space - O(1)
    """
    # null check
    if len(ordered_list) == 0:
      return False
    elif len(ordered_list) < 2:
      return ordered_list[0] == number
      
    start, end = 0, len(ordered_list)

    while start <= end:
      mid = start + (end - start)//2

      if ordered_list[mid] == number:
        return True
      elif number > ordered_list[mid]:
        start = mid + 1
      elif number < ordered_list[mid]:
        end = mid - 1

    return False


# Tests
class Test(unittest.TestCase):

    def test_empty_list(self):
        result = contains([], 1)
        self.assertFalse(result)

    def test_one_item_list_number_present(self):
        result = contains([1], 1)
        self.assertTrue(result)

    def test_one_item_list_number_absent(self):
        result = contains([1], 2)
        self.assertFalse(result)

    def test_small_list_number_present(self):
        result = contains([2, 4, 6], 4)
        self.assertTrue(result)

    def test_small_list_number_absent(self):
        result = contains([2, 4, 6], 5)
        self.assertFalse(result)

    def test_large_list_number_present(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 8)
        self.assertTrue(result)

    def test_large_list_number_absent(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 0)
        self.assertFalse(result)

    def test_large_list_number_first(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 1)
        self.assertTrue(result)

    def test_large_list_number_last(self):
        result = contains([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 10)
        self.assertTrue(result)


unittest.main(verbosity=2)