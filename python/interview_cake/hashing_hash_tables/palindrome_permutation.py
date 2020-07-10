import unittest
import itertools


def has_palindrome_permutation(the_string):

    # Check if any permutation of the input is a palindrome
    """
    Task: Check whether the given string has any permutation which is a palindrome

    Algorithm:
      1. Find all permutations of the string
      2. iterate through permutations and check if is palindrome
      3. if any are a palindrome, we will return true
    """    

    perm_list = itertools.permutations(the_string)

    def yield_permutations(lst):
      if len(lst) == 0:
        yield []
      elif len(lst) == 1:
        yield lst
      else:
        for i in range(len(lst)):
          x = lst[i]
          xs = lst[:i] + lst[i+1:]
          for p in yield_permutations(xs):
            yield [x] + p

    def is_palindrome(string):
      start, end = 0, len(string) - 1

      while start < end:
        if string[start] == string[end]:
          start += 1
          end -= 1
        else:
          return False
      return True

    for el in perm_list:
      if is_palindrome(el):
        return True
    return False



# Tests

class Test(unittest.TestCase):

    def test_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcbcd')
        self.assertTrue(result)

    def test_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabccbdd')
        self.assertTrue(result)

    def test_no_permutation_with_odd_number_of_chars(self):
        result = has_palindrome_permutation('aabcd')
        self.assertFalse(result)

    def test_no_permutation_with_even_number_of_chars(self):
        result = has_palindrome_permutation('aabbcd')
        self.assertFalse(result)

    def test_empty_string(self):
        result = has_palindrome_permutation('')
        self.assertTrue(result)

    def test_one_character_string(self):
        result = has_palindrome_permutation('a')
        self.assertTrue(result)


unittest.main(verbosity=2)