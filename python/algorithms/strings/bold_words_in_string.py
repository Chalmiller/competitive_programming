from typing import *
import collections

class Solution:
    def boldWords(self, words: List[str], S: str) -> str:
      let_collection = set()
      bold_characters = [False] * len(S)

      for word in words:
        word_index = S.find(word)
        for i in range(word_index, word_index + len(word)): 
          bold_characters[i] = True
          
      ans = ""
      index = 0

      while index < len(S):
        if bold_characters[index] == True:
          ans += r'<b>'
          while index < len(S) and bold_characters[index]:
            ans += S[index]
            index += 1
          ans += r'<b>'
        else:
          ans += S[index]
          index += 1
      return ans
        
obj = Solution()
print(obj.boldWords(["ab", "bc"], "aabcd"))
