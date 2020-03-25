class Solution:
    def tribonacci(self, n: int) -> int:
        a, b, c = 1, 0, 0
        for _ in xrange(n): a, b, c = b, c, a + b + c
        return c
