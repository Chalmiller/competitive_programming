# 1309: Decrypt String from Alphabet to IntegerMapping
from typing import *

class Solution:
    def freqAlphabets(self, s: str) -> str:
        new_string = []
        for index, num in enumerate(s):
            if (num == "#"):
                last_num = "".join(s[index-2:index])
                new_string.pop()
                new_string.pop()
                new_string.append(chr(int(last_num) + 96))
            elif int(num) < 10 and int(num) >= 0:
                new_string.append(chr(int(num) + 96)) 
        return "".join(new_string)
        """
        one line solution using regex
        return ''.join(chr(int(i[:2]) + 96) for i in re.findall(r'\d\d#|\d', s))
        """

obj = Solution()
num = obj.freqAlphabets("12345678910#11#12#13#14#15#16#17#18#19#20#21#22#23#24#25#26#")
print(num)
