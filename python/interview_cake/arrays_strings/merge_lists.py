import unittest


def merge_lists(my_list, alices_list):

    # Combine the sorted lists into one large sorted list
    """
    Task: Merge the two lists into one.

    Algorithm:
      1. generate a place holder list
      2. keep track of three pointers, one for each list
      3. compare each element and insert into the new list
      4. return new list
    """

    merge_list = []
    i, j, k = 0, 0, 0

    while j < len(alices_list) and i < len(my_list):

      if my_list[i] < alices_list[j]:
        merge_list.append(my_list[i])
        i += 1
      else:
        merge_list.append(alices_list[j])
        j += 1
    
    while j <= len(alices_list) - 1:
      merge_list.append(alices_list[j])
      j += 1

    while i <= len(my_list) - 1:
      merge_list.append(my_list[i])
      i += 1
    
    return merge_list

merge_lists([3, 4, 6, 10, 11, 15], [1, 5, 8, 12, 14, 19])

# Tests

# class Test(unittest.TestCase):

#     def test_both_lists_are_empty(self):
#         actual = merge_lists([], [])
#         expected = []
#         self.assertEqual(actual, expected)

#     def test_first_list_is_empty(self):
#         actual = merge_lists([], [1, 2, 3])
#         expected = [1, 2, 3]
#         self.assertEqual(actual, expected)

#     def test_second_list_is_empty(self):
#         actual = merge_lists([5, 6, 7], [])
#         expected = [5, 6, 7]
#         self.assertEqual(actual, expected)

#     def test_both_lists_have_some_numbers(self):
#         actual = merge_lists([2, 4, 6], [1, 3, 7])
#         expected = [1, 2, 3, 4, 6, 7]
#         self.assertEqual(actual, expected)

#     def test_lists_are_different_lengths(self):
#         actual = merge_lists([2, 4, 6, 8], [1, 7])
#         expected = [1, 2, 4, 6, 7, 8]
#         self.assertEqual(actual, expected)


# unittest.main(verbosity=2)