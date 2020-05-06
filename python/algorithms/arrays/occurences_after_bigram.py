from typing import *

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        result = []
        text_list = text.split()
        print(text_list)
        for index in range(len(text_list) - 2):
          if text_list[index] == first and text_list[index + 1] == second:
            result.append(text_list[index + 2])
        return result

obj = Solution()
print(obj.findOcurrences("alice is aa good girl she is a good student", "a", "good"))