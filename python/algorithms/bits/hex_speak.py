from typing import *

class Solution:
    def toHexspeak(self, num: str) -> str:
        hex_num = hex(int(num))[2:]

        valid_chars = {'A', 'B', 'C', 'D', 'E', 'F', 'I', 'O'}
        hex_num = hex_num.replace('1', 'I').replace('0', 'O').upper()

        for let in hex_num:
          if let not in valid_chars:
            return "ERROR"
        return hex_num

obj = Solution()
print(obj.toHexspeak('747823223228'))

        
