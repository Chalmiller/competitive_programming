from typing import *

class Solution:
    def defangIPaddr(self, address: str) -> str:
        return address.replace('.', '[.]')

obj = Solution()
string = obj.defangIPaddr("255.100.50.0")
print(string)