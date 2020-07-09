import unittest


def reverse_words(message):

    """
    Task: Return the message in reverse order
    
    Algorithm: 
        1. join the strings into a single string
        2. split them based on spaces
        3. reverse the list 
        4. rejoin the list with spaces
    """
    
    word_list = "".join(message)
    new_list = word_list.split(" ")
    new_list.reverse()
    break_list = []
    
    for el in new_list:
        for let in el:
            break_list.append(let)
        break_list.append(" ")

    for i, let in enumerate(break_list):
      if i == len(break_list) - 1:
        break
      else:
        message[i] = let
    print(message)
    

print(reverse_words([ 'c', 'a', 'k', 'e', ' ',
            'p', 'o', 'u', 'n', 'd', ' ',
            's', 't', 'e', 'a', 'l' ]))


# Tests

# class Test(unittest.TestCase):

#     def test_one_word(self):
#         message = list('vault')
#         reverse_words(message)
#         expected = list('vault')
#         self.assertEqual(message, expected)

#     def test_two_words(self):
#         message = list('thief cake')
#         reverse_words(message)
#         expected = list('cake thief')
#         self.assertEqual(message, expected)

#     def test_three_words(self):
#         message = list('one another get')
#         reverse_words(message)
#         expected = list('get another one')
#         self.assertEqual(message, expected)

#     def test_multiple_words_same_length(self):
#         message = list('rat the ate cat the')
#         reverse_words(message)
#         expected = list('the cat ate the rat')
#         self.assertEqual(message, expected)

#     def test_multiple_words_different_lengths(self):
#         message = list('yummy is cake bundt chocolate')
#         reverse_words(message)
#         expected = list('chocolate bundt cake is yummy')
#         self.assertEqual(message, expected)

#     def test_empty_string(self):
#         message = list('')
#         reverse_words(message)
#         expected = list('')
#         self.assertEqual(message, expected)


# unittest.main(verbosity=2)