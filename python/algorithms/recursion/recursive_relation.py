import unittest

class Solution:
    def power_power(self, n, a=3, b=2):
        def power(b, n):
            if n == 0: return 1
            return b * power(b, n-1)
        if b == 0: return 1
        return a * power(a, power(b,n) - 1)

class TestPower(unittest.TestCase):
    def test_power_0(self):
        n = 0
        output = 3
        self.assertEqual(output, Solution().power_power(n))
    
    def test_power_1(self):
        n = 1
        output = 9
        self.assertEqual(output, Solution().power_power(n))
    
    def test_power_2(self):
        n = 2
        output = 81
        self.assertEqual(output, Solution().power_power(n))
    
    def test_power_3(self):
        n = 3
        output = 6561
        self.assertEqual(output, Solution().power_power(n))

unittest.main(verbosity=2)