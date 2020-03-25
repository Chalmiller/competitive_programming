#  1281: Subtract the Product and Sum of Digits of an Integer

from functools import *

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        A = map(int, str(n))
        return reduce(operator.mul, A) - sum(A)
