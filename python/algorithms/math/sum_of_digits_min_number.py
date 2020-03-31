# 1085: Sum of Digits in the Minimum Number
from typing import *

class Solution:
    def sumOfDigits(self, A: List[int]) -> int:
        min_digit = min(A)
        digit_sum = 0
        for i in str(min_digit):
            digit_sum += int(i)
        if digit_sum % 2 == 1:
            return 0
        else:
            return 1
