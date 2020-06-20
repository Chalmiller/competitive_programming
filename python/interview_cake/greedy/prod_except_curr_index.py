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
      raise ValueError("We needa few more values than that")
    if int_list.count(0) > 1:
      return [0 for _ in range(len(int_list))]

    total_prod = reduce(operator.mul, int_list)
    res_list = []

    for i, el in enumerate(int_list):
      if el == 0:
        temp_list = list(filter(lambda x: x > 0, int_list))
        curr_prod = reduce(operator.mul, temp_list)
        res_list.append(curr_prod)
      else:
        res_list.append(total_prod//el)

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