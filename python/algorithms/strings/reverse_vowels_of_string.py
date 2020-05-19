from typing import *

class Solution:
    def reverseVowels(self, s: str) -> str:
      vowels = {'a', 'e', 'i', 'o', 'u'}
      str_list = [let for let in s]
      reversed_vowel_index = [index for index, let in enumerate(s) if let.lower() in vowels]
      print(reversed_vowel_index)

      def swap_let(string_list, index1, index2):
        string_list[index1], string_list[index2] = string_list[index2], string_list[index1]
        return string_list

      low, high = 0, len(reversed_vowel_index) - 1
      print(low, high)
      while low < high:
        swap_let(str_list, reversed_vowel_index[low], reversed_vowel_index[high])
        low += 1
        high -= 1

      return "".join(str_list)

obj = Solution()
print(obj.reverseVowels("leetcode"))
