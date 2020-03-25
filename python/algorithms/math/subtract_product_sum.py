from functools import *

class Solution:
    def subtractProductAndSum(self, n: int) -> int:
        A = map(int, str(n))
        return reduce(operator.mul, A) - sum(A)
