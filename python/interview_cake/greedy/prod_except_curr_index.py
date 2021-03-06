import unittest
from functools import reduce
import operator


def get_products_of_all_ints_except_at_index(int_list):

    """
    Task: For each index of the list, replace with the product of the rest of the elements

    Algorithm:
    1. If we are allowed to use division, we can just take the product once and divide it
      by the element at each index
    """
    if len(int_list) < 2:
      raise ValueError("We need a few more values than that")
    if int_list.count(0) > 1:
      return [0 for _ in range(len(int_list))]

    temp_array = [0] * len(int_list)
    temp_array[0] = reduce(operator.mul, int_list[1:])
    temp_array[-1] = reduce(operator.mul, int_list[:-2])
    for i in range(1, len(int_list)):
        curr_list = int_list[:i] + int_list[i+1:]
        temp_array[i] = reduce(operator.mul, curr_list)
    
    int_list = temp_array[:]

    return int_list

# Tests
class Test(unittest.TestCase):

    def test_small_list(self):
        actual = get_products_of_all_ints_except_at_index([1, 2, 3])
        expected = [6, 3, 2]
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = get_products_of_all_ints_except_at_index([8, 2, 4, 3, 1, 5])
        expected = [120, 480, 240, 320, 960, 192]
        self.assertEqual(actual, expected)

    def test_list_has_one_zero(self):
        actual = get_products_of_all_ints_except_at_index([6, 2, 0, 3])
        expected = [0, 0, 36, 0]
        self.assertEqual(actual, expected)

    def test_list_has_two_zeros(self):
        actual = get_products_of_all_ints_except_at_index([4, 0, 9, 1, 0])
        expected = [0, 0, 0, 0, 0]
        self.assertEqual(actual, expected)

    def test_one_negative_number(self):
        actual = get_products_of_all_ints_except_at_index([-3, 8, 4])
        expected = [32, -12, -24]
        self.assertEqual(actual, expected)

    def test_all_negative_numbers(self):
        actual = get_products_of_all_ints_except_at_index([-7, -1, -4, -2])
        expected = [-8, -56, -14, -28]
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            get_products_of_all_ints_except_at_index([1])


unittest.main(verbosity=2)