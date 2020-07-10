from typing import *

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        """
        Task: Basically, we just add 1 to the number that the array respresents

        Algorithm:
          1. Convert the array into a string
          2. convert that string to a number
          3. increment by one
          4. convert back to string
          5. break string into an array of integers
        """
        str_list = [str(num) for num in digits]
        number = "".join(str_list)
        _int = int(number)
        _int += 1
        str_conversion = str(_int)
        res_list = [int(digit) for digit in str_conversion]

        return res_list
        

obj = Solution()
print(obj.plusOne([4,3,2,1]))
        