# 709: To Lower Case
from typing import *

class Solution:
    def toLowerCase(self, str: str) -> str:
        new_string_list =[]
        for let in str:
            if let.isupper():
                new_string_list.append(chr(ord(let) + 32))
            else:
                new_string_list.append(let)
        return "".join(new_string_list)

obj = Solution()
num = obj.toLowerCase("Hello")
print(num)
