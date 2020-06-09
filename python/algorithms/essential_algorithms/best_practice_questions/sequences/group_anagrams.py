from typing import *
from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """
        Task: given an input list of strings, group the anagrams into a list of lists

        Intuition: 
          - My brute force approach would be to iterate through the list and sort the first string.
            Iterate through the list again sort each item after it and compare to the initial sorted
            string. Generate a tuple for the matches within the list and place into a set after 
            every loop. 
        Pseudo Code:
        1. sort the first string
        2. iterate through the rest looking for matches by sorting each item
        3. place the matches into a set with tuple matches
        """
        anagram_cache = defaultdict(list)

        for word in strs:
          anagram = tuple(sorted(word))
          anagram_cache[anagram].append(word)
        
        response = [group for group in anagram_cache.values()]
        return response

obj = Solution()
print(obj.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
