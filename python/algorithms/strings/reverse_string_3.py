# 557: Reverse Words in a String
from typing import *

class Solution:
    def reverseWords(self, s: str) -> str:
        stack = []
        reverse_word = []
        for let in s:
            stack.append(ord(let))
        for num in range(len(stack)):
            reverse_word.append(chr(stack.pop()))
        return "".join(reverse_word)

obj = Solution()
num = obj.reverseWords("Let's take LeetCode contest")
print(num)
