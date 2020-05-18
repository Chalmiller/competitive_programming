from typing import *

class Solution:
    def addStrings(self, num1: str, num2: str) -> str:
        num1_int = 0
        for let in num1:
          num1_int = num1_int*10 + ord(let) - 48

        num2_int = 0
        for let in num2:
          num2_int = num2_int*10 + ord(let) - 48

        return str(num1_int + num2_int)

        