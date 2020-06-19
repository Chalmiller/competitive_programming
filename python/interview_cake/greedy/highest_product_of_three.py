import unittest
import math


def highest_product_of_3(list_of_ints):

    # Calculate the highest product of three numbers
    """
    Task: Calculate the highest product of three integers in the list

    Intuition:
      - This could be handled by a max heap in which we pop off the three largest values
      - iteratively we could go start out with the frist three being the highest, then we
        could replace the values in the new list with any value that is higher than the min
        val of the list, finally ending the algorithm by returning the product of the list.
      - There's also the three pointer approach, but that would take n^3 time to execute...

    Algorithm:
    1. 
    """
    if len(list_of_ints) < 3:
      raise ValueError("There must be at least three values present in the input list")

    highest_prod_of_3 = list_of_ints[0] * list_of_ints[1]* list_of_ints[2]
    highest_prod_of_2 = list_of_ints[0] * list_of_ints[1]
    highest = max(list_of_ints[0], list_of_ints[1])
    lowest_prod_of_2 = list_of_ints[0] * list_of_ints[1]
    lowest = min(list_of_ints[0], list_of_ints[1])

    for i in range(2, len(list_of_ints)):
      curr = list_of_ints[i]

      highest_prod_of_3 = max(highest_prod_of_3,
                              curr * highest_prod_of_2,
                              curr * lowest_prod_of_2)
      highest_prod_of_2 = max(highest_prod_of_2,
                              curr * highest,
                              curr * lowest)
      highest = max(curr, highest)
      lowest_prod_of_2 = min(lowest_prod_of_2,
                              curr * lowest,
                              curr * highest)
      lowest = min(curr, lowest)

    return highest_prod_of_3
    
# Tests
class Test(unittest.TestCase):

    def test_short_list(self):
        actual = highest_product_of_3([1, 2, 3, 4])
        expected = 24
        self.assertEqual(actual, expected)

    def test_longer_list(self):
        actual = highest_product_of_3([6, 1, 3, 5, 7, 8, 2])
        expected = 336
        self.assertEqual(actual, expected)

    def test_list_has_one_negative(self):
        actual = highest_product_of_3([-5, 4, 8, 2, 3])
        expected = 96
        self.assertEqual(actual, expected)

    def test_list_has_two_negatives(self):
        actual = highest_product_of_3([-10, 1, 3, 2, -10])
        expected = 300
        self.assertEqual(actual, expected)

    def test_list_is_all_negatives(self):
        actual = highest_product_of_3([-5, -1, -3, -2])
        expected = -6
        self.assertEqual(actual, expected)

    def test_error_with_empty_list(self):
        with self.assertRaises(Exception):
            highest_product_of_3([])

    def test_error_with_one_number(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1])

    def test_error_with_two_numbers(self):
        with self.assertRaises(Exception):
            highest_product_of_3([1, 1])


unittest.main(verbosity=2)