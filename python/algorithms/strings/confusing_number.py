from typing import *

class Solution:
    def confusingNumber(self, N: int) -> bool:
        confusing_nums = {"6":"9", "0":"0", '1':"1", "8":"8", "9":"6"}
        invalid = [2,3,4,5,7]
        reversed_string = reversed(str(N))
        rotated_string = []
        for num in reversed_string:
          if int(num) in invalid:
            return False
          else:
            rotated_string.append(confusing_nums[num])

        mirrored = int("".join(rotated_string))
        return mirrored != N

obj = Solution()
print(obj.confusingNumber(89))

        
