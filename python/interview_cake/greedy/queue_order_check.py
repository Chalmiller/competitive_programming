import unittest


def is_first_come_first_served(take_out_orders, dine_in_orders, served_orders):

    # Check if we're serving orders first-come, first-served
    """
    Task: merge the take out and dine in orders into a single list and determine 
          if it is strictly increasing.
    Intuition: This seems otbe optimally a merge sort problem. Though, for the brute force
          I would just iterate through both lists and place the smallest element in each time

    Algorithm:
    1. merge the two lists into a new list
    2. return whether the served orders are equal to that return list
    """
    i, j, k, n, m = 0, 0, 0, len(take_out_orders)-1, len(dine_in_orders)-1
    merge_list = []

    while i <= n and j <= m:
      print(i, j)
      if take_out_orders[i] < dine_in_orders[j]:
        merge_list.append(take_out_orders[i])
        i += 1
      elif take_out_orders[i] > dine_in_orders[j]:
        merge_list.append(dine_in_orders[j])
        j += 1
      k += 1
      print(merge_list)
    
    print(i, j)
    if i < n:
      merge_list.extend(take_out_orders[i:])
    if j < m:
      merge_list.extend(take_out_orders[j:])
    
    print(merge_list)
    return merge_list == served_orders

print(is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6]))
    

# # Tests
# class Test(unittest.TestCase):

#     def test_both_registers_have_same_number_of_orders(self):
#         result = is_first_come_first_served([1, 4, 5], [2, 3, 6], [1, 2, 3, 4, 5, 6])
#         self.assertTrue(result)

#     def test_registers_have_different_lengths(self):
#         result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 6, 3, 5])
#         self.assertFalse(result)

#     def test_one_register_is_empty(self):
#         result = is_first_come_first_served([], [2, 3, 6], [2, 3, 6])
#         self.assertTrue(result)

#     def test_served_orders_is_missing_orders(self):
#         result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 6, 3, 5])
#         self.assertFalse(result)

#     def test_served_orders_has_extra_orders(self):
#         result = is_first_come_first_served([1, 5], [2, 3, 6], [1, 2, 3, 5, 6, 8])
#         self.assertFalse(result)

#     def test_one_register_has_extra_orders(self):
#         result = is_first_come_first_served([1, 9], [7, 8], [1, 7, 8])
#         self.assertFalse(result)

#     def test_one_register_has_unserved_orders(self):
#         result = is_first_come_first_served([55, 9], [7, 8], [1, 7, 8, 9])
#         self.assertFalse(result)

#     def test_order_numbers_are_not_sequential(self):
#         result = is_first_come_first_served([27, 12, 18], [55, 31, 8], [55, 31, 8, 27, 12, 18])
#         self.assertTrue(result)


# unittest.main(verbosity=2)